# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 1. Association Example: Pre-existing Conditions and Premiums
print("Association Example:")
data = {
    'Has_Preexisting_Condition': [1, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    'Premium': [1000, 600, 1200, 700, 1100, 1300, 650, 700, 1150, 600]
}
df = pd.DataFrame(data)
association = df.corr(method='spearman')
print(association)
print("\n")

# 2. Dependence Example: Payment Amount Based on Insurance Coverage
print("Dependence Example:")
data = {
    'Has_Insurance': [1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    'Out_of_Pocket_Payment': [200, 150, 1000, 250, 900, 950, 180, 850, 220, 160]
}
df = pd.DataFrame(data)
print(df)
print("\n")

# 3. Correlation Example: Age and Health Insurance Claims
print("Correlation Example:")
data = {
    'Age': [25, 35, 45, 55, 65, 75, 30, 40, 50, 60],
    'Number_of_Claims': [1, 2, 2, 3, 4, 5, 1, 2, 3, 4]
}
df = pd.DataFrame(data)
correlation, _ = pearsonr(df['Age'], df['Number_of_Claims'])
print(f"Correlation between Age and Number of Claims: {correlation}")
print("\n")

# 4. Causation Example: Smoking and Health Insurance Premiums
print("Causation Example:")
data = {
    'Smoker': [1, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    'Premium': [1500, 700, 1600, 800, 1550, 1650, 750, 800, 1580, 700]
}
df = pd.DataFrame(data)
correlation, _ = pearsonr(df['Smoker'], df['Premium'])
print(f"Correlation between Smoking and Premium: {correlation}")
# Causation is inferred based on domain knowledge, not just correlation
print("\n")

# 5. Covariance Example: Preventive Check-ups and Claims
print("Covariance Example:")
data = {
    'Preventive_Checkups': [5, 7, 6, 8, 9, 4, 3, 7, 6, 5],
    'Number_of_Claims': [1, 1, 2, 1, 0, 3, 4, 1, 2, 3]
}
df = pd.DataFrame(data)
covariance = np.cov(df['Preventive_Checkups'], df['Number_of_Claims'])[0][1]
print(f"Covariance between Preventive Checkups and Number of Claims: {covariance}")
print("\n")

# 6. Simpson's Paradox Example
print("Simpson's Paradox Example:")
data = {
    'Hospital': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'Age_Group': ['<50', '<50', '50+', '50+', '<50', '<50', '50+', '50+'],
    'Approved': [30, 50, 20, 40, 60, 80, 50, 70],
    'Total': [40, 60, 30, 50, 100, 120, 70, 90]
}
df = pd.DataFrame(data)
df['Approval_Rate'] = df['Approved'] / df['Total']
print("Approval Rates by Hospital and Age Group:")
print(df)

# Overall approval rate
total_approved = df['Approved'].sum()
total_cases = df['Total'].sum()
overall_approval_rate = total_approved / total_cases
print(f"\nOverall Approval Rate: {overall_approval_rate:.2f}")
