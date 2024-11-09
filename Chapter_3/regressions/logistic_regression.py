import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample Data: Health Insurance Data (Age, Smoking Status, Obesity vs. Likelihood of High Claim)
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Smoker': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],  # 0 = Non-smoker, 1 = Smoker
    'Obese': [0, 0, 1, 1, 0, 1, 1, 0, 1, 1],  # 0 = Not Obese, 1 = Obese
    'High_Claim': [0, 1, 0, 1, 0, 1, 1, 0, 1, 1]  # 0 = No High Claim, 1 = High Claim
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features (Age, Smoker, Obese) and Target (High Claim Likelihood)
X = df[['Age', 'Smoker', 'Obese']]  # Feature matrix
y = df['High_Claim']  # Target vector

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions using the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

# Plotting decision boundaries (simplified for 2D visualization)
plt.scatter(df['Age'], df['High_Claim'], c=df['High_Claim'], cmap='viridis', marker='o', edgecolor='k')
plt.xlabel('Age')
plt.ylabel('High Claim Likelihood')
plt.title('Logistic Regression: High Claim Prediction')
plt.show()
