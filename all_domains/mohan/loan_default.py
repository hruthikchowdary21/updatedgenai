import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Path to the CSV file on your local machine
file_path = r'C:\Users\hruth\GENAI\all_domains\mohan\Loan_default_original.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Get a concise summary of the DataFrame
print("\nData Summary:")
df.info()  # Display info about the DataFrame

# Generate descriptive statistics for all columns
print("\nDescriptive Statistics for All Columns:")
print(df.describe(include='all'))  # include='all' to describe all columns, including non-numeric

# Set pandas options to display all columns
pd.set_option('display.max_columns', None)

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Drop the LoanID column for analysis
df = df.drop(columns=['LoanID'], errors='ignore')  # Ensure LoanID is not included

# Convert object columns to int where applicable
# Example: If you have categorical columns that can be mapped to integers
# You can adjust the mapping based on your specific dataset
for column in df.select_dtypes(include=['object']).columns:
    if df[column].nunique() == 2:  # If the column has only two unique values
        df[column] = df[column].map({df[column].unique()[0]: 0, df[column].unique()[1]: 1})
    else:
        df[column] = df[column].astype('category').cat.codes  # Convert to category and then to codes

# Ensure the Default column is binary (0 and 1)
df['Default'] = df['Default'].map({'No': 0, 'Yes': 1})  # Adjust mapping based on your data

# Check for NaN values in the target variable
if df['Default'].isnull().any():
    print("\nNaN values found in the Default column. Dropping rows with NaN values.")
    df = df.dropna(subset=['Default'])  # Drop rows where Default is NaN

# Identify categorical columns for encoding
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Identify numeric columns for analysis
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

# Select features and target variable
X = df.drop(columns=['Default'])  # Features (excluding the target variable)
y = df['Default']  # Target variable

# Check for NaN values in features
if X.isnull().any().any():
    print("\nNaN values found in feature columns. Dropping rows with NaN values.")
    df = df.dropna()  # Drop rows with any NaN values in features

# Check if there are enough samples left
if df.shape[0] == 0:
    raise ValueError("No samples left after dropping NaN values. Please check your data.")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression(max_iter=1000)  # Increase max_iter if convergence issues occur
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"\nAccuracy: {accuracy}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)
