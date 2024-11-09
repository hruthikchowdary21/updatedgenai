import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Path to the CSV file on your local machine
file_path = r'C:\Users\hruth\GENAI\all_domains\lahari\Student_performance_data _.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Set pandas options to display all columns and avoid line breaks
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Prevent line breaks in the output

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Get a concise summary of the DataFrame
print("\nData Summary:")
print(df.info())

# Generate descriptive statistics for all columns
print("\nDescriptive Statistics for All Columns:")
print(df.describe(include='all'))  # include='all' to describe all columns, including non-numeric

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Visualize the distribution of numeric columns
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
for column in numeric_columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Create box plots for specified columns to visualize outliers
columns_to_check = ['ParentalSupport', 'StudyTimeWeekly', 'Absences']
plt.figure(figsize=(12, 8))
for i, column in enumerate(columns_to_check, 1):
    plt.subplot(1, 3, i)  # Create a grid of subplots (1 row, 3 columns)
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the plots

# Create pair plots to visualize relationships and potential outliers
sns.pairplot(df[numeric_columns])
plt.suptitle('Pair Plots of Student Performance Data', y=1.02)  # Adjust title position
plt.show()  # Display the plots

# Calculate the correlation matrix for specific columns
columns_of_interest = ['Age', 'ParentalEducation', 'StudyTimeWeekly', 'Absences', 
                        'Tutoring', 'ParentalSupport', 'Extracurricular', 'GPA', 'GradeClass']
correlation_matrix = df[columns_of_interest].corr()

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Heatmap of Correlation Matrix for Selected Columns')
plt.show()  # Display the heatmap

# Linear Regression
# Select features and target variable
X = df[['Age', 'ParentalEducation', 'StudyTimeWeekly', 'Absences']]  # Example features
y = df['GPA']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nMean Squared Error: {mse}")
print(f"R² Score: {r2}")

# Plot predicted vs actual values
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Diagonal line
plt.title('Predicted vs Actual GPA')
plt.xlabel('Actual GPA')
plt.ylabel('Predicted GPA')
plt.xlim([y.min(), y.max()])
plt.ylim([y.min(), y.max()])
plt.grid()
plt.show()
