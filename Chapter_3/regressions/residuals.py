import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample Data: Health Insurance Data (Age vs. Insurance Cost)
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Insurance_Cost': [2000, 2500, 3000, 3200, 3500, 4000, 4200, 4500, 5000, 5200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Feature (Age) and Target (Insurance Cost)
X = df[['Age']]  # Feature matrix
y = df['Insurance_Cost']  # Target vector

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions using the test set
y_pred = model.predict(X_test)

# Calculate residuals
residuals = y_test - y_pred

# Print residuals
print("Residuals:")
print(residuals)

# Plotting residuals
plt.scatter(X_test, residuals, color='red')
plt.axhline(y=0, color='blue', linestyle='--')
plt.xlabel('Age')
plt.ylabel('Residuals (Actual - Predicted)')
plt.title('Residual Plot: Age vs. Residuals')
plt.show()
