import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the CSV file into a DataFrame
file_path = r'C:\Users\hruth\GENAI\all_domains\sathvik\updated_ecommerce_dataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Get a concise summary of the DataFrame
print("\nData Summary:")
print(df.info())

# Generate descriptive statistics for all columns
print("\nDescriptive Statistics for All Columns:")
print(df.describe(include='all'))

# Convert categorical variables to numeric
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})  # Male: 1, Female: 0
df['Device_Used'] = df['Device_Used'].astype('category').cat.codes  # Convert Device_Used to category codes
df['Product_Category'] = df['Product_Category'].astype('category').cat.codes  # Convert Product_Category to category codes

# Display the updated DataFrame
print("\nData after converting categorical variables:")
print(df.head())

# Create a heatmap for the correlation of the columns
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()  # Calculate the correlation matrix
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Heatmap of Correlation Matrix')
plt.show()  # Display the heatmap

# Prepare data for logistic regression
X = df.drop(columns=['Purchased'])  # Features
y = df['Purchased']  # Target variable

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
plt.ylabel('Predicted Probability of Purchased = 1')
plt.xticks([0, 1])
plt.grid()
plt.show()  # Display the logistic regression plot
