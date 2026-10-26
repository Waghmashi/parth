# Real Estate House Price Prediction

## About the Project
This project uses machine learning to estimate house prices from property details. It compares several regression models and looks at how their predictions perform on data that was not used for training.

The supplied dataset contains 4,200 property records. The target column is `house_price_inr`. The `house_id` column is an identifier, so it is not used as a model feature.

## Project Goals
- Explore the dataset and check its quality.
- Predict prices using Simple Linear Regression.
- Use multiple property features with Multiple Linear Regression.
- Test Polynomial Regression for curved relationships.
- Evaluate predictions with standard regression metrics.
- Implement Batch, Stochastic, and Mini-Batch Gradient Descent.
- Compare model errors and discuss overfitting, underfitting, and the bias–variance trade-off.

## Dataset
The data contains property details such as house area, bedrooms, bathrooms, location score, property age, and house price. The notebook checks the real column names and data quality before training models.

## Models Used
- **Simple Linear Regression:** Uses house area as the only input feature.
- **Multiple Linear Regression:** Uses the selected property features together.
- **Polynomial Regression:** Adds polynomial terms for house area to model a possible curved relationship.
- **Gradient Descent:** Demonstrates Batch, Stochastic, and Mini-Batch updates that aim to reduce prediction error.

## Evaluation Metrics
- **MSE:** Mean squared prediction error; lower is better.
- **MAE:** Average absolute prediction error, in the same units as house price.
- **RMSE:** Square root of MSE, also in price units; lower is better.
- **R²:** Indicates how much variation in house prices is explained by the model.
- **Adjusted R²:** Adjusts R² based on the number of predictors.

## Project Files
- `Real_Estate_House_Price_Regression.ipynb` — notebook with code, saved outputs, tables, and charts.
- `RealEstate_HousePrice_Dataset.xlsx` — dataset used in the project.
- `README.md` — project description and instructions.

## Requirements
Python 3, Jupyter Notebook or JupyterLab, and these libraries:
- pandas
- numpy
- matplotlib
- scikit-learn
- openpyxl

Install the libraries if needed:

```bash
python -m pip install pandas numpy matplotlib scikit-learn openpyxl jupyter
```

## How to Run
1. Download and extract the project ZIP.
2. Keep the notebook and Excel dataset in the same folder.
3. Open Jupyter Notebook or JupyterLab.
4. Open `Real_Estate_House_Price_Regression.ipynb`.
5. Select **Kernel → Restart Kernel and Run All Cells**.
6. Review the output tables, graphs, and final report.

The notebook uses `random_state=42` for a repeatable train/test split.

## Understanding the Results
Compare MAE and RMSE to see the size of prediction errors. Compare R² and Adjusted R² to assess how well each model explains price variation. Residual plots help identify patterns that a straight-line model may not capture. A large gap between training and test errors can be a warning sign of overfitting.

The notebook ranks the compared models using test RMSE. A practical model choice should also consider simplicity, reliability, and the intended use.

## Conclusion
This project demonstrates a complete introductory workflow for house-price prediction: exploring data, training regression models, evaluating results, visualizing relationships, and comparing optimization methods. Predicted prices are estimates rather than guaranteed market values. Before real-world use, a model should be checked on newer data and monitored over time.

**Learning note:** Review the notebook and make sure you can explain the features, models, metrics, graphs, and final conclusion in your own words.
