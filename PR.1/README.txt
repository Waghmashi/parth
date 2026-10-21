## Project Title
Predictive Insight Engine: House Price Prediction using Supervised Learning

## What is this Project About?
This project predicts house prices based on features like area, location, bedrooms, age, etc. 
It uses Supervised Learning algorithms to build a model that a real estate company can use 
to estimate the price of a house.

## Dataset Used
File Name: RealEstate_HousePrice_Dataset_4200.csv

Columns:
- house_id : Unique ID for each house
- area_sqft : Size of house in square feet
- bedrooms : Number of bedrooms
- bathrooms : Number of bathrooms
- location_score : Rating of the location (1-10)
- age_years : How old is the house
- distance_city_km : Distance from city center
- lot_size_sqft : Total plot size
- has_garage : 1 = Yes, 0 = No
- has_pool : 1 = Yes, 0 = No
- renovation_years_ago : How many years since last renovation
- house_price_inr : Price of house (Target Variable)

## Tools and Libraries Used
- Python
- Pandas (for data handling)
- NumPy (for math calculations)
- Matplotlib and Seaborn (for graphs)
- Scikit-learn (for machine learning models)

## Steps Performed in the Notebook

1. Import Libraries
   - Imported pandas, numpy, matplotlib, seaborn, and sklearn.

2. Load Dataset
   - Loaded the CSV file and viewed the first 5 rows.

3. Identify Variables (Task 7)
   - X = Independent Variables (all features except house_price_inr and house_id)
   - y = Dependent Variable (house_price_inr)

4. Data Visualization (Task 8)
   - Created a Correlation Heatmap to see which features affect price.
   - Created a Scatter Plot of Area vs Price.
   - Found that area_sqft and location_score are most important.

5. Train Test Split (Task 9)
   - Split data into 80% Training and 20% Testing.
   - Training data: 3360 rows
   - Testing data: 840 rows

6. Simple Linear Regression (Task 10-12)
   - Used only area_sqft to predict price.
   - Plotted the Regression Line.
   - Printed Slope and Intercept.
   - Checked Residual Distribution (should be normal).

7. Model Evaluation Metrics (Task 13-14)
   - Calculated MSE, MAE, RMSE, R2, and Adjusted R2.
   - R2 was around 0.45, meaning only 45% of price is explained by area alone.

8. Multiple Linear Regression (Task 15-17)
   - Used all features to predict price.
   - R2 improved to around 0.79.
   - This model performed much better than Simple Regression.

9. Polynomial Regression (Task 18-20)
   - Tried Degree 2 and Degree 3.
   - R2 was around 0.81.
   - But the curve was too wavy, showing signs of Overfitting.

10. Gradient Descent from Scratch (Task 21-25)
    - Implemented Batch Gradient Descent.
    - Implemented Stochastic Gradient Descent (SGD).
    - Implemented Mini-Batch Gradient Descent.
    - All three methods found similar theta values.
    - Plotted the Cost vs Epochs graph to show convergence.

11. Bias-Variance Analysis (Task 26-28)
    - Simple Linear Regression = Underfitting (High Bias)
    - Multiple Linear Regression = Good Fit (Balanced)
    - Polynomial Regression = Overfitting (High Variance)

12. Final Report (Task 29-30)
    - Summarized findings and submitted.

## Key Results

| Model | R2 Score | Verdict |
|-------|----------|---------|
| Simple Linear Regression | 0.45 | Underfitting |
| Multiple Linear Regression | 0.79 | Best Model |
| Polynomial Regression (Degree 2) | 0.81 | Overfitting |

## Best Model
Multiple Linear Regression is the best model because:
- It uses all features (area, location, bedrooms, etc.)
- It gives a stable R2 score of 0.79
- It does not overfit like Polynomial Regression

## Business Interpretation
The company should focus on buying houses with:
- Bigger area (area_sqft)
- Better location score (location_score)
Because these two factors drive the price up the most.

## What I Learned
1. More features lead to better predictions.
2. Higher R2 score is not always better (Polynomial overfitted).
3. Gradient Descent is used to minimize error by updating weights.
4. Bias-Variance Trade-off is important to avoid overfitting and underfitting.

