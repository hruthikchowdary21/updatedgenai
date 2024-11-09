import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score


# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\hruth\GENAI\all_domains\hruthik\insurance.csv')  # Use raw string for the file path

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Get a concise summary of the DataFrame
print("\nData Summary:")
print(df.info())
pd.set_option('display.max_columns', None)

# Generate descriptive statistics for all columns except specified ones
excluded_columns = ['payment_type', 'tip_amount', 'imp_surcharge', 'pickup_location_id', 'dropoff_location_id']
eda_columns = df.drop(columns=excluded_columns, errors='ignore')  # Drop excluded columns

print("\nDescriptive Statistics for Selected Columns:")
print(eda_columns.describe(include='all'))  # include='all' to describe all columns, including non-numeric

# Initialize LabelEncoders
le_sex = LabelEncoder()
le_smoker = LabelEncoder()
le_region = LabelEncoder()

# Apply Label Encoding
df['sex'] = le_sex.fit_transform(df['sex'])
df['smoker'] = le_smoker.fit_transform(df['smoker'])
df['region'] = le_region.fit_transform(df['region'])

# Print the mapping of encoded values to original categories
print("Sex mapping:", dict(enumerate(le_sex.classes_)))
print("Smoker mapping:", dict(enumerate(le_smoker.classes_)))
print("Region mapping:", dict(enumerate(le_region.classes_)))

# Create a new DataFrame to count the number of smokers and non-smokers
smoking_status = df['smoker'].value_counts()

# Prepare data for plotting
smoking_status_by_sex = df.groupby(['sex', 'smoker']).size().unstack(fill_value=0)

# Prepare data for plotting
labels = ['Non-Smokers', 'Smokers']
counts_female = smoking_status_by_sex.loc[0]  # Assuming 0 is Female
counts_male = smoking_status_by_sex.loc[1]    # Assuming 1 is Male

# Plotting the results
plt.figure(figsize=(8, 5))
bar_width = 0.35
x = np.arange(len(labels))

# Create bars for females and males
plt.bar(x - bar_width/2, counts_female, width=bar_width, color='orange', label='Females')
plt.bar(x + bar_width/2, counts_male, width=bar_width, color='blue', label='Males')

plt.title('Count of Smokers and Non-Smokers by Sex')
plt.xlabel('Smoking Status')
plt.ylabel('Count')
plt.xticks(x, labels)
plt.legend()
plt.show()

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display the correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()

# Define independent variables (X) and the dependent variable (y)
X = df[['sex', 'smoker', 'region', 'age', 'bmi', 'children']]
y = df['expenses']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate Mean Squared Error and R² value
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Scatter plot of actual vs predicted expenses
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Diagonal line
plt.xlabel('Actual Expenses')
plt.ylabel('Predicted Expenses')
plt.title('Actual vs Predicted Expenses')
plt.show()
