import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the CSV file into a DataFrame
file_path = r'C:\Users\hruth\GENAI\all_domains\naga_sai\Healthcare-Diabetes.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Get a concise summary of the DataFrame
print("\nData Summary:")
print(df.info())

# Generate descriptive statistics for all columns except 'Id'
print("\nDescriptive Statistics for Selected Columns:")
print(df.drop(columns=['Id'], errors='ignore').describe())

# Create a heatmap for the correlation of the remaining columns
plt.figure(figsize=(12, 8))
correlation_matrix = df.drop(columns=['Id'], errors='ignore').corr()  # Calculate the correlation matrix
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Heatmap of Correlation Matrix')
plt.show()  # Display the heatmap

# Prepare data for logistic regression
X = df.drop(columns=['Id', 'Outcome'], errors='ignore')  # Features
y = df['Outcome']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression(max_iter=200)  # Increase max_iter if convergence issues occur
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()  # Display the confusion matrix plot

# Logistic Regression Plot
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_proba, alpha=0.6, color='blue')
plt.axhline(0.5, color='red', linestyle='--')  # Decision boundary
plt.title('Logistic Regression: Predicted Probabilities vs Actual Outcomes')
plt.xlabel('Actual Outcome')
plt.ylabel('Predicted Probability of Outcome = 1')
plt.xticks([0, 1])
plt.grid()
plt.show()  # Display the logistic regression plot
