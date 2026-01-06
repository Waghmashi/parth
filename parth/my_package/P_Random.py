import random
import string

# 1. Generate random number
def p_generate_number():
    num = random.randrange(1, 102)
    print("Random Number :-", num)


# 2. Create random number list
def p_generate_list():
    size = int(input("Enter list size: "))
    result = []

    for _ in range(size):
        result.append(random.randint(1, 100))

    print(" List:-", result)


# 3. Generate random password
def p_generate_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits
    pwd = ""

    for _ in range(length):
        pwd = pwd + random.choice(chars)

    print("Generated Password:", pwd)


# 4. Generate OTP
def p_generate_otp():
    otp = ""
    count = 0

    while count < 4:
        otp += str(random.randint(0, 9))
        count += 1

    print("OTP:-", otp)
