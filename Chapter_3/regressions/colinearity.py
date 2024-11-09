import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler

# Sample Data: Health Insurance Data (Age, BMI, Weight, Height)
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'BMI': [22, 24, 26, 28, 30, 32, 33, 35, 36, 37],
    'Weight': [68, 75, 80, 85, 90, 95, 100, 105, 110, 115],  # in kg
    'Height': [1.75, 1.80, 1.75, 1.78, 1.80, 1.82, 1.76, 1.79, 1.81, 1.83]  # in meters
}

# Create a DataFrame
df = pd.DataFrame(data)

# Correlation Matrix to Visualize Collinearity
print("Correlation Matrix:")
corr_matrix = df.corr()
print(corr_matrix)

# Plot the Correlation Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix for Health Insurance Variables')
plt.show()

# Calculate Variance Inflation Factor (VIF) for each feature
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
vif_data = pd.DataFrame()
vif_data['Feature'] = df.columns
vif_data['VIF'] = [variance_inflation_factor(df_scaled, i) for i in range(df_scaled.shape[1])]

print("\nVariance Inflation Factor (VIF):")
print(vif_data)

# Interpretation: High VIF (> 10) indicates high collinearity.
