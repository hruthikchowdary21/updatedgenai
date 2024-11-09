import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# Setting random seed for reproducibility
np.random.seed(0)

# Generate synthetic data directly
data = {
    'Age': np.random.randint(18, 65, size=1000),
    'BMI': np.random.normal(28, 5, size=1000),
    'Smoking_Status': np.random.choice(['Non-smoker', 'Smoker'], size=1000, p=[0.8, 0.2]),
    'Exercise_Frequency': np.random.choice(['None', 'Low', 'Medium', 'High'], size=1000, p=[0.1, 0.3, 0.4, 0.2]),
    'Pre_Existing_Conditions': np.random.choice([0, 1], size=1000, p=[0.7, 0.3]),
    'Previous_Medical_Costs': np.random.uniform(200, 2000, size=1000)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('health_insurance.csv', index=False)
print("Data saved to 'health_insurance.csv'.")

# Print basic statistics
print(df.describe())

# Histogram of Ages
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Boxplot of Medical Costs by Smoking Status
plt.figure(figsize=(10, 6))
sns.boxplot(x='Smoking_Status', y='Previous_Medical_Costs', data=df)
plt.title('Medical Costs by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Medical Costs')
plt.show()

# Statistical testing
smoker_costs = df[df['Smoking_Status'] == 'Smoker']['Previous_Medical_Costs']
non_smoker_costs = df[df['Smoking_Status'] == 'Non-smoker']['Previous_Medical_Costs']
t_stat, p_value = ttest_ind(smoker_costs, non_smoker_costs)
print("T-test results -- t-statistic:", t_stat, "p-value:", p_value)

# Regression analysis
features = df.drop('Previous_Medical_Costs', axis=1)
target = df['Previous_Medical_Costs']

# One-hot encoding for categorical variables
categorical_features = ['Smoking_Status', 'Exercise_Frequency', 'Pre_Existing_Conditions']
one_hot = OneHotEncoder()

# Create a preprocessing and modeling pipeline
preprocessor = ColumnTransformer(transformers=[
    ('cat', one_hot, categorical_features)
], remainder='passthrough')

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

# Fit model
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.5)
plt.title('Comparison of Actual vs. Predicted Medical Costs')
plt.xlabel('Actual Costs')
plt.ylabel('Predicted Costs')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)  # Adds a reference line
plt.show()
