import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to the CSV file on your local machine
file_path = r'C:/Users/hruth/GENAI/all_domains/sriram/AP_Industrial_Policy_Dataset.csv'

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

    # Create pair plots to visualize relationships and potential outliers for numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    sns.pairplot(df[numeric_columns])
    plt.suptitle('Pair Plots of AP Industrial Policy Data', y=1.02)  # Adjust title position
    plt.show()  # Display the plots

    # Calculate the correlation matrix for numeric columns
    correlation_matrix = df[numeric_columns].corr()

    # Create a heatmap to visualize the correlation matrix
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Heatmap of Correlation Matrix for Numeric Columns')
    plt.show()  # Display the heatmap

except Exception as e:
    print(f"An error occurred: {e}")

