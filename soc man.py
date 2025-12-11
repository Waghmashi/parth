# app/api/v1/endpoints/payments.py (continued)

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid
from datetime import datetime

from app.core.database import get_db
from app.models import MaintenancePayment, MaintenanceRecord, BankTransaction
from app.schemas import PaymentCreate, BankTransferRequest
from app.services.payment_service import PaymentService
from app.utils.security import get_current_user

router = APIRouter()

@router.post("/online")
async def initiate_online_payment(
    payment_data: PaymentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Initiate online payment"""
    # Get maintenance record
    stmt = select(MaintenanceRecord).where(
        MaintenanceRecord.id == payment_data.maintenance_id
    )
    result = await db.execute(stmt)
    record = result.scalar_one_or_none()
    
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maintenance record not found"
        )
    
    # Check if already paid
    if record.is_paid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maintenance already paid"
        )
    
    # Create payment record
    payment = MaintenancePayment(
        maintenance_id=payment_data.maintenance_id,
        payer_id=current_user.id,
        amount=payment_data.amount,
        payment_method=payment_data.payment_method,
        status="pending",
        transaction_id=str(uuid.uuid4())
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    
    # Process payment based on method
    if payment_data.payment_method == "stripe":
        payment_intent = await PaymentService.create_stripe_payment_intent(
            amount=payment_data.amount,
            metadata={
                "payment_id": str(payment.id),
                "maintenance_id": str(payment_data.maintenance_id),
                "user_id": str(current_user.id)
            }
        )
        return {
            "payment_id": payment.id,
            "client_secret": payment_intent["client_secret"],
            "payment_intent_id": payment_intent["payment_intent_id"]
        }
    
    elif payment_data.payment_method == "razorpay":
        order = await PaymentService.create_razorpay_order(
            amount=payment_data.amount,
            receipt=f"maintenance_{payment_data.maintenance_id}"
        )
        return {
            "payment_id": payment.id,
            "razorpay_order_id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"]
        }
    
    elif payment_data.payment_method == "upi":
        # Generate UPI payment link
        upi_id = f"society@bank"
        return {
            "payment_id": payment.id,
            "upi_link": f"upi://pay?pa={upi_id}&pn=Society Management&am={payment_data.amount}",
            "qr_code_url": f"https://api.qrserver.com/v1/create-qr-code/?data=upi://pay?pa={upi_id}&am={payment_data.amount}"
        }
    
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported payment method"
        )

@router.post("/bank-transfer")
async def process_bank_transfer(
    transfer_data: BankTransferRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Process bank transfer payment"""
    # Get maintenance record
    stmt = select(MaintenanceRecord).where(
        MaintenanceRecord.id == transfer_data.maintenance_id
    )
    result = await db.execute(stmt)
    record = result.scalar_one_or_none()
    
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maintenance record not found"
        )
    
    # Check if already paid
    if record.is_paid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maintenance already paid"
        )
    
    # Process bank transfer
    transfer_result = await PaymentService.process_bank_transfer(
        bank_name=transfer_data.bank_name,
        account_number=transfer_data.account_number,
        ifsc_code=transfer_data.ifsc_code,
        amount=transfer_data.amount,
        utr_number=transfer_data.utr_number
    )
    
    # Create payment record
    payment = MaintenancePayment(
        maintenance_id=transfer_data.maintenance_id,
        payer_id=current_user.id,
        amount=transfer_data.amount,
        payment_method="bank_transfer",
        status="completed" if transfer_result["status"] == "success" else "failed",
        transaction_id=transfer_result["transaction_id"],
        payment_date=datetime.now(),
        gateway_response=transfer_result
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    
    # Create bank transaction record
    bank_transaction = BankTransaction(
        payment_id=payment.id,
        bank_reference=transfer_result["bank_reference"],
        utr_number=transfer_data.utr_number,
        bank_name=transfer_data.bank_name,
        account_number=transfer_data.account_number,
        ifsc_code=transfer_data.ifsc_code,
        transaction_date=datetime.now(),
        status="completed"
    )
    db.add(bank_transaction)
    
    # Update maintenance record if payment successful
    if transfer_result["status"] == "success":
        record.is_paid = True
        record.updated_at = datetime.now()
    
    await db.commit()
    
    return {
        "message": "Bank transfer processed successfully",
        "payment_id": payment.id,
        "transaction_id": payment.transaction_id,
        "status": payment.status,
        "bank_reference": transfer_data.utr_number
    }

@router.get("/history")
async def get_payment_history(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
    page: int = 1,
    limit: int = 10
):
    """Get payment history"""
    offset = (page - 1) * limit
    
    if current_user.role in ["admin", "accountant"]:
        # Admins can see all payments
        stmt = select(MaintenancePayment).join(MaintenanceRecord).join(MaintenanceRecord.flat)
    else:
        # Residents can only see their own payments
        stmt = select(MaintenancePayment).where(
            MaintenancePayment.payer_id == current_user.id
        )
    
    # Add pagination
    stmt = stmt.offset(offset).limit(limit).order_by(MaintenancePayment.payment_date.desc())
    
    result = await db.execute(stmt)
    payments = result.scalars().all()
    
    # Count total
    count_stmt = select(func.count()).select_from(MaintenancePayment)
    if current_user.role not in ["admin", "accountant"]:
        count_stmt = count_stmt.where(MaintenancePayment.payer_id == current_user.id)
    
    count_result = await db.execute(count_stmt)
    total = count_result.scalar()
    
    return {
        "payments": payments,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "pages": (total + limit - 1) // limit
        }
    }

@router.get("/bank-details")
async def get_bank_details():
    """Get society bank details for direct transfer"""
    return {
        "bank_name": settings.BANK_NAME,
        "account_number": settings.BANK_ACCOUNT_NUMBER,
        "ifsc_code": settings.BANK_IFSC_CODE,
        "account_name": "Society Management Account",
        "branch": "Main Branch"
    }
    # app/utils/security.py
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.config import settings
from app.core.database import get_db
from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
# app/api/v1/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import timedelta

from app.core.database import get_db
from app.schemas import Token, UserCreate, UserInDB
from app.models import User
from app.utils.security import (
    verify_password, get_password_hash,
    create_access_token, get_current_user
)

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(User).where(User.username == form_data.username)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserInDB)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    # Check if user already exists
    stmt = select(User).where(User.email == user_data.email)
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    user = User(
        email=user_data.email,
        username=user_data.email.split('@')[0],  # Use email prefix as username
        full_name=user_data.full_name,
        hashed_password=hashed_password,
        phone=user_data.phone,
        role=user_data.role
    )
    
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    return user

@router.get("/me", response_model=UserInDB)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
# app/api/v1/endpoints/analytics.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from datetime import datetime, timedelta
import calendar

from app.core.database import get_db
from app.models import (
    MaintenanceRecord, MaintenancePayment, 
    User, Flat, Complaint
)
from app.schemas import AnalyticsResponse
from app.utils.security import get_current_user

router = APIRouter()

@router.get("/dashboard", response_model=AnalyticsResponse)
async def get_dashboard_analytics(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get dashboard analytics"""
    if current_user.role not in ["admin", "accountant", "manager"]:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )
    
    # Total collection
    total_collection_stmt = select(func.sum(MaintenancePayment.amount)).where(
        MaintenancePayment.status == "completed"
    )
    total_collection_result = await db.execute(total_collection_stmt)
    total_collection = total_collection_result.scalar() or 0
    
    # Pending amount
    pending_stmt = select(func.sum(MaintenanceRecord.amount)).where(
        MaintenanceRecord.is_paid == False
    )
    pending_result = await db.execute(pending_stmt)
    pending_amount = pending_result.scalar() or 0
    
    # Total residents
    residents_stmt = select(func.count(User.id)).where(User.role == "resident")
    residents_result = await db.execute(residents_stmt)
    total_residents = residents_result.scalar() or 0
    
    # Active complaints
    active_complaints_stmt = select(func.count(Complaint.id)).where(
        Complaint.status.in_(["pending", "in_progress"])
    )
    active_complaints_result = await db.execute(active_complaints_stmt)
    active_complaints = active_complaints_result.scalar() or 0
    
    # Monthly trend (last 6 months)
    monthly_trend = []
    today = datetime.now()
    
    for i in range(6):
        month = today.month - i
        year = today.year
        if month <= 0:
            month += 12
            year -= 1
        
        month_start = datetime(year, month, 1)
        if month == 12:
            month_end = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            month_end = datetime(year, month + 1, 1) - timedelta(days=1)
        
        # Collection for the month
        collection_stmt = select(func.sum(MaintenancePayment.amount)).where(
            and_(
                MaintenancePayment.status == "completed",
                MaintenancePayment.payment_date >= month_start,
                MaintenancePayment.payment_date <= month_end
            )
        )
        collection_result = await db.execute(collection_stmt)
        month_collection = collection_result.scalar() or 0
        
        monthly_trend.append({
            "month": f"{calendar.month_abbr[month]} {year}",
            "collection": month_collection,
            "pending": 0  # Can add pending calculation if needed
        })
    
    monthly_trend.reverse()  # Show oldest to newest
    
    return AnalyticsResponse(
        total_collection=total_collection,
        pending_amount=pending_amount,
        total_residents=total_residents,
        active_complaints=active_complaints,
        monthly_trend=monthly_trend
    )

@router.get("/financial-summary")
async def get_financial_summary(
    year: int = datetime.now().year,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get yearly financial summary"""
    if current_user.role not in ["admin", "accountant"]:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )
    
    monthly_summary = []
    
    for month in range(1, 13):
        month_start = datetime(year, month, 1)
        if month == 12:
            month_end = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            month_end = datetime(year, month + 1, 1) - timedelta(days=1)
        
        # Total generated
        generated_stmt = select(func.sum(MaintenanceRecord.amount)).where(
            and_(
                MaintenanceRecord.month == month,
                MaintenanceRecord.year == year
            )
        )
        generated_result = await db.execute(generated_stmt)
        generated = generated_result.scalar() or 0
        
        # Total collected
        collected_stmt = select(func.sum(MaintenancePayment.amount)).where(
            and_(
                MaintenancePayment.status == "completed",
                MaintenancePayment.payment_date >= month_start,
                MaintenancePayment.payment_date <= month_end
            )
        )
        collected_result = await db.execute(collected_stmt)
        collected = collected_result.scalar() or 0
        
        monthly_summary.append({
            "month": calendar.month_name[month],
            "generated": generated,
            "collected": collected,
            "pending": generated - collected,
            "collection_rate": (collected / generated * 100) if generated > 0 else 0
        })
    
    return {
        "year": year,
        "monthly_summary": monthly_summary,
        "total_generated": sum(item["generated"] for item in monthly_summary),
        "total_collected": sum(item["collected"] for item in monthly_summary)
    }
    # app/api/v1/endpoints/complaints.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import List, Optional

from app.core.database import get_db
from app.models import Complaint
from app.schemas import ComplaintCreate, ComplaintUpdate
from app.utils.security import get_current_user

router = APIRouter()

@router.post("/", response_model=dict)
async def create_complaint(
    complaint_data: ComplaintCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Create new complaint"""
    complaint = Complaint(
        resident_id=current_user.id,
        **complaint_data.dict()
    )
    
    db.add(complaint)
    await db.commit()
    await db.refresh(complaint)
    
    return {
        "message": "Complaint created successfully",
        "complaint_id": complaint.id
    }

@router.get("/", response_model=List[dict])
async def get_complaints(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
    status: Optional[str] = None,
    priority: Optional[int] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    """Get complaints with filters"""
    offset = (page - 1) * limit
    
    # Build query based on user role
    if current_user.role in ["admin", "manager"]:
        stmt = select(Complaint)
    else:
        stmt = select(Complaint).where(Complaint.resident_id == current_user.id)
    
    # Apply filters
    if status:
        stmt = stmt.where(Complaint.status == status)
    if priority:
        stmt = stmt.where(Complaint.priority == priority)
    
    # Add pagination
    stmt = stmt.offset(offset).limit(limit).order_by(Complaint.created_at.desc())
    
    result = await db.execute(stmt)
    complaints = result.scalars().all()
    
    return complaints

@router.put("/{complaint_id}")
async def update_complaint(
    complaint_id: str,
    update_data: ComplaintUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Update complaint status/resolution"""
    stmt = select(Complaint).where(Complaint.id == complaint_id)
    result = await db.execute(stmt)
    complaint = result.scalar_one_or_none()
    
    if not complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )
    
    # Check permissions
    if current_user.role not in ["admin", "manager"] and complaint.resident_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )
    
    # Update fields
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(complaint, field, value)
    
    complaint.updated_at = datetime.now()
    await db.commit()
    
    return {"message": "Complaint updated successfully"}
# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from app.core.database import get_db
from app.models import User, Flat
from app.schemas import UserCreate, UserUpdate, UserInDB
from app.utils.security import get_current_user, get_password_hash

router = APIRouter()

@router.get("/", response_model=List[UserInDB])
async def get_users(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
    role: str = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    """Get users with pagination and filters"""
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )
    
    offset = (page - 1) * limit
    stmt = select(User)
    
    if role:
        stmt = stmt.where(User.role == role)
    
    stmt = stmt.offset(offset).limit(limit)
    result = await db.execute(stmt)
    users = result.scalars().all()
    
    return users

@router.get("/{user_id}/flats")
async def get_user_flats(
    user_id: str,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get flats owned by a user"""
    # Check permissions
    if current_user.role not in ["admin", "manager"] and str(current_user.id) != user_id:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )
    
    stmt = select(Flat).where(Flat.owner_id == user_id)
    result = await db.execute(stmt)
    flats = result.scalars().all()
    
    return flats

@router.put("/{user_id}")
async def update_user(
    user_id: str,
    update_data: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Update user information"""
    # Check permissions
    if current_user.role not in ["admin"] and str(current_user.id) != user_id:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )
    
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    # Update fields
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(user, field, value)
    
    user.updated_at = datetime.now()
    await db.commit()
    
    return {"message": "User updated successfully"}
# run.py
import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )