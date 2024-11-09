import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix

# Path to the CSV file on your local machine
file_path = r'C:/Users/hruth/GENAI/all_domains/gayatri/apples_quality.csv'

# Load the CSV file into a DataFrame
try:
    # Read the CSV file, handling bad lines
    df = pd.read_csv(file_path, on_bad_lines='warn')  # 'warn' will print a warning for bad lines

    # Display the first few rows of the DataFrame
    print("Initial Data:")
    print(df.head())

    # Convert 'Quality' column from object to numerical values (0 for 'bad', 1 for 'good')
    df['Quality'] = df['Quality'].replace({'bad': 0, 'good': 1})

    # Get a concise summary of the DataFrame
    print("\nData Summary:")
    print(df.info())

    # Generate descriptive statistics for all columns except 'id'
    print("\nDescriptive Statistics for All Columns (excluding 'id'):")
    print(df.drop(columns=['id']).describe(include='all'))  # Exclude 'id' from description

    # Set pandas options to display all columns
    pd.set_option('display.max_columns', None)

    # Check for missing values
    print("\nMissing Values in Each Column:")
    print(df.isnull().sum())

    # Visualize the distribution of numeric columns (excluding 'id')
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    numeric_columns.remove('id') if 'id' in numeric_columns else None  # Ensure 'id' is excluded
    for column in numeric_columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], bins=30, kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    # Create pair plots to visualize relationships and potential outliers (excluding 'id')
    sns.pairplot(df[numeric_columns])
    plt.suptitle('Pair Plots of Apple Quality Data (excluding id)', y=1.02)  # Adjust title position
    plt.show()  # Display the plots

    # Prepare data for prediction
    X = df.drop(columns=['Quality', 'id'])  # Features (excluding 'Quality' and 'id')
    y = df['Quality']  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the logistic regression model
    model = LogisticRegression(max_iter=200)  # Increase max_iter if convergence issues occur
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class

    # Evaluate the model
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Plot predicted probabilities
    plt.figure(figsize=(10, 5))
    plt.hist(y_pred_proba, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Predicted Probabilities of Quality (Good)')
    plt.xlabel('Predicted Probability')
    plt.ylabel('Frequency')
    plt.axvline(x=0.5, color='red', linestyle='--')  # Threshold line
    plt.show()

    # Calculate the correlation matrix for numeric columns (excluding 'id')
    correlation_matrix = df[numeric_columns].corr()

    # Create a heatmap to visualize the correlation matrix
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Heatmap of Correlation Matrix (excluding id)')
    plt.show()  # Display the heatmap

except Exception as e:
    print(f"An error occurred: {e}")
