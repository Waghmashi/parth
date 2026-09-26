Customer Credit Risk Data Preparation Project

About This Project

This is my final project for the Data Preprocessing course. In this project, I worked on a Customer Credit Risk dataset. The main aim was to clean the raw data and make it ready for machine learning so that we can predict whether a customer will default on a loan or not.

The dataset had 1,01,000 rows and 15 columns. It came from different sources, so there were many missing values, outliers, and different types of data. I solved all these problems step by step.

What I Did (Step by Step)

1. Loaded and Understood the Data
   First, I loaded the CSV file using Pandas. Then I used head(), info(), and describe() to understand the data. I found that:
   - Columns like age, annual_income, credit_score, and spending_ratio had missing values.
   - Columns like gender, region, education_level, employment_type, and loan_purpose were text (categorical) columns.
   - join_date was a date column that needed separate handling.

2. Filled Missing Values
   I did not delete the missing values because I did not want to lose data. So:
   - For numbers (age, income, credit score), I filled the missing values with the mean (average).
   - For text columns (like employment_type), I filled the missing values with the mode (most common value).
   After this, there were 0 missing values left in the dataset.

3. Removed Outliers
   Some customers had very high income and loan amounts compared to others. These values can confuse the model. So I used the IQR (Interquartile Range) method to cap these extreme values. I did not delete the rows, I only adjusted the values.

4. Handled the Date Column
   From the join_date column, I extracted Year, Month, and Day. This will help the model understand time-based patterns. I dropped the original date column after extraction.

5. Converted Text to Numbers (Encoding)
   Computers cannot understand text, so:
   - I used Label Encoding for gender and education_level (converted to 0, 1, 2...).
   - I used One-Hot Encoding for region, employment_type, and loan_purpose, which created new columns.

6. Feature Scaling
   Income was in thousands and age was between 20-50. This confuses the model. So I used StandardScaler to bring all numeric columns to the same scale.

7. Created New Features
   I created two new features:
   - Debt-to-Income Ratio = loan_amount / annual_income (this shows how big the loan is compared to income).
   - Average Monthly Transactions = transaction_count / 6 (average over 6 months).
   These features are very useful for the model.

Final Result

At the end, the data was completely clean and ready. The final shape was (101000, 24). I saved the cleaned data as cleaned_credit_risk_data.csv. I also made a heatmap to show which features are most related to default_flag.