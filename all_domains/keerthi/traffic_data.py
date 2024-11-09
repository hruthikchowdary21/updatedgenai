import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# Path to the CSV file on your local machine
file_path = r'C:\Users\hruth\GENAI\all_domains\keerthi\Metro_Interstate_Traffic_Volume.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Get a concise summary of the DataFrame
print("\nData Summary:")
print(df.info())

# Generate descriptive statistics for all columns
print("\nDescriptive Statistics for All Columns:")
print(df.describe(include='all'))  # include='all' to describe all columns, including non-numeric

# Set pandas options to display all columns
pd.set_option('display.max_columns', None)

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Drop rows with missing values (if any)
df = df.dropna()

# Convert 'weather_main' column to int by assigning numbers for each condition
weather_mapping = {
    'Clear': 1,
    'Clouds': 2,
    'Rain': 3,
    'Snow': 4,
    'Mist': 5,
    'Fog': 6,
    'Drizzle': 7,
    'Thunderstorm': 8,
    'Haze': 9,
    'Dust': 10,
    'Sand': 11,
    'Ash': 12,
    'Squall': 13,
    'Tornado': 14
}

# Replace weather conditions with corresponding integers
df['weather_main'] = df['weather_main'].replace(weather_mapping)

# Check the data type of the 'weather_main' column after conversion
print("\nData Types After Conversion:")
print(df.dtypes)

# Identify categorical columns (excluding the target variable)
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

# One-hot encode categorical variables
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Prepare data for prediction
X = df.drop(columns=['traffic_volume'])  # Features (excluding 'traffic_volume')
y = df['traffic_volume']  # Target variable

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
plt.title('Predicted vs Actual Traffic Volume')
plt.xlabel('Actual Traffic Volume')
plt.ylabel('Predicted Traffic Volume')
plt.xlim([y.min(), y.max()])
plt.ylim([y.min(), y.max()])
plt.grid()
plt.show()

# Optional: Plot residuals
plt.figure(figsize=(10, 5))
residuals = y_test - y_pred
sns.histplot(residuals, bins=30, kde=True)
plt.title('Residuals Distribution')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.axvline(0, color='red', linestyle='--')  # Line at zero
plt.show()
