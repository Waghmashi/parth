Customer Purchase Behavior Analyzer

In this project, I worked on customer purchase behavior. I had 3 different 
files - one CSV, one JSON, and one SQL file. My goal was to load all three, 
clean them, and make one final dataset that can be used for machine learning.

Files I Used:
1. users.csv     - Customer details (name, age, gender, city, etc.)
2. sales.json    - Sales transactions (who bought what, how much they paid)
3. inventory.sql - Product details (product name, category, price, stock)

What I Did (Step by Step):

1. Data Loading
   I loaded all three files separately. For CSV, I used pd.read_csv. 
   For JSON, I used json.load. For SQL, I connected using sqlite3 and 
   ran a query.

2. Checked Missing Values
   When I looked at the data, I found that the users table had some missing 
   values in age and gender. Sales and inventory had no missing values.

3. Filled Missing Values
   I filled the missing values in the age column with the average (mean). 
   I filled the missing values in the gender column with the most common 
   value (mode). After this, there were 0 missing values left.

4. Removed Outliers
   Some customers had very high amounts and some products had very high 
   prices. These values can confuse the model. So I used the IQR 
   (Interquartile Range) method to cap these values. I did not delete any 
   rows, I only adjusted the values.

5. Handled Date Columns
   The users table had registration_date and the sales table had date. 
   I extracted Year, Month, and Day from both. This will help the model 
   understand time-based patterns. I dropped the original date columns.

6. Converted Text to Numbers (Encoding)
   Computers cannot understand text, so I used LabelEncoder. I converted 
   gender, city, payment_type, and category columns into numbers.

7. Merged All Three Data
   I merged the sales data with users data (based on user_id), and then 
   merged it with inventory data (based on product_id). This created one 
   complete dataset with customer, transaction, and product information 
   all in one place.

8. Created New Features
   I created 3 new columns:
   - total_spend = amount * price (how much money was spent)
   - tax = total_spend * 0.18 (18% tax)
   - final_amount = total_spend + tax (total amount to pay)

9. Feature Scaling
   Income and price were in thousands, and age was between 18-50. This 
   confuses the model. So I used StandardScaler to bring all numeric 
   columns to the same scale.

Final Result:
- Final file name: final_cleaned_dataset.csv
- Total rows: 1000
- Total columns: 20+
- All missing values filled
- All outliers handled
- Text columns converted to numbers
- New features created
- Data is completely clean and ready