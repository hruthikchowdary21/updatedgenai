import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Path to the CSV file on your local machine
file_path = r'C:\Users\hruth\GENAI\all_domains\jyothsna\dailyActivity_merged.csv'

# Load the CSV file into a DataFrame
try:
    # Read the CSV file
    df = pd.read_csv(file_path, on_bad_lines='warn')  # 'warn' will print a warning for bad lines

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

    # Drop 'date' and 'id' columns if they exist
    df = df.drop(columns=['ActivityDate', 'Id'], errors='ignore')  # Use errors='ignore' to avoid errors if columns are not present

    # Create a list of numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    # Visualize the distribution of numeric columns
    for column in numeric_columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], bins=30, kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    # Create pair plots to visualize relationships and potential outliers for numeric columns
    sns.pairplot(df[numeric_columns])
    plt.suptitle('Pair Plots of Daily Activity Data (excluding date and id)', y=1.02)  # Adjust title position
    plt.show()  # Display the plots

    # Calculate the correlation matrix for numeric columns
    correlation_matrix = df[numeric_columns].corr()

    # Create a heatmap to visualize the correlation matrix
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Heatmap of Correlation Matrix for Numeric Columns (excluding date and id)')
    plt.show()  # Display the heatmap

    # Prepare data for prediction
    X = df.drop(columns=['Calories'])  # Features (excluding 'Calories')
    y = df['Calories']  # Target variable

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
    plt.title('Predicted vs Actual Calories')
    plt.xlabel('Actual Calories')
    plt.ylabel('Predicted Calories')
    plt.xlim([y.min(), y.max()])
    plt.ylim([y.min(), y.max()])
    plt.grid()
    plt.show()

    # Plot residuals
    plt.figure(figsize=(10, 5))
    residuals = y_test - y_pred
    sns.histplot(residuals, bins=30, kde=True)
    plt.title('Residuals Distribution')
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    plt.axvline(0, color='red', linestyle='--')  # Line at zero
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
