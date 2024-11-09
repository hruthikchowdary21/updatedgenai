import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\hruth\GENAI\PCA_and_kfold\titanic.csv')  # Adjust the path as needed

# Data Cleaning: Select relevant columns
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]

# Check for missing values
print("\nData Summary:")
print(df.info())

# Fill missing values for 'Age' with the median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing values for 'Fare' with the median
df['Fare'].fillna(df['Fare'].median(), inplace=True)

# Encode 'Sex' to numeric values (male: 0, female: 1)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# EDA: Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# EDA: Visualize potential outliers using box plots
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Age', 'Fare', 'SibSp', 'Parch']])
plt.title('Box Plots for Outlier Detection')
plt.show()

# Visualize the survival rate
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', data=df, palette='pastel')
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['Not Survived', 'Survived'])
plt.show()

# Bubble Chart: Age vs Fare colored by Survival status
plt.figure(figsize=(12, 8))
plt.scatter(data=df, x='Age', y='Fare', s=df['SibSp']*50, c='Survived', alpha=0.5, cmap='viridis', edgecolors='w')
plt.title('Bubble Chart: Age vs Fare (Bubble Size = SibSp)')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.colorbar(label='Survived (0 = No, 1 = Yes)')
plt.grid(True)
plt.show()

# Define features and target variable
X = df.drop(columns=['Survived'])
y = df['Survived']

# Split the data into training (70%) and testing (30%) sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)

# Further split the temporary set into validation (10%) and testing (20%)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.67, random_state=42)  # 0.67 of 30% is 20%

# K-Fold Cross-Validation
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)

# Initialize a model
model = LogisticRegression(max_iter=200)

# Store accuracy for each fold
fold_accuracies = []

for train_index, val_index in kf.split(X_train):
    X_kf_train, X_kf_val = X_train.iloc[train_index], X_train.iloc[val_index]
    y_kf_train, y_kf_val = y_train.iloc[train_index], y_train.iloc[val_index]
    
    # Fit the model
    model.fit(X_kf_train, y_kf_train)
    
    # Validate the model
    y_kf_pred = model.predict(X_kf_val)
    accuracy = accuracy_score(y_kf_val, y_kf_pred)
    fold_accuracies.append(accuracy)

# Print the results
print(f"\nFold Accuracies: {fold_accuracies}")
print(f"Mean Accuracy: {np.mean(fold_accuracies):.4f}")

# Final evaluation on the test set
model.fit(X_train, y_train)  # Fit on the entire training set
y_test_pred = model.predict(X_test)
print("\nTest Set Evaluation:")
print(classification_report(y_test, y_test_pred)) 