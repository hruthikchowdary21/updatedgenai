import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create a DataFrame to view the dataset
iris_df = pd.DataFrame(data=X, columns=iris.feature_names)
iris_df['Target'] = y

# Display the first few rows of the dataset
print("Original Iris Dataset:")
print(iris_df.head())

# Standardize the features (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Display the standardized data
print("\nStandardized Data:")
print(pd.DataFrame(X_scaled, columns=iris.feature_names).head())

# Split the dataset into training (70%), testing (20%), and validation (10%)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)  # 30% for temp (testing + validation)
X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.3333, random_state=42)  # 10% validation from the temp set

# Initialize PCA and reduce the dimensionality
pca = PCA(n_components=2)  # Reduce the dimensions to 2
X_pca = pca.fit_transform(X_train)

# Check explained variance ratio
explained_variance = pca.explained_variance_ratio_
print("\nExplained Variance Ratio:")
print(explained_variance)

# Check if the explained variance meets the threshold
if sum(explained_variance) >= 0.95:
    print("The explained variance meets the threshold of 0.95.")
else:
    print("The explained variance does not meet the threshold of 0.95.")

# Create a DataFrame with the PCA results
pca_df = pd.DataFrame(data=X_pca, columns=['Principal Component 1', 'Principal Component 2'])
pca_df['Target'] = y_train

# Fit the model using the training set
model = LogisticRegression()
model.fit(X_pca, y_train)

# Make predictions on the test set
X_test_pca = pca.transform(X_test)  # Transform the test set using the same PCA
y_pred = model.predict(X_test_pca)

# Calculate accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
print(f"\nTest Set Accuracy: {accuracy:.2f}")

# K-Fold Cross Validation on the training set
kf = KFold(n_splits=5, shuffle=True, random_state=42)

fold = 1
for train_index, test_index in kf.split(X_pca):
    X_train_kf, X_test_kf = X_pca[train_index], X_pca[test_index]
    y_train_kf, y_test_kf = y_train[train_index], y_train[test_index]
    
    # Fit the model
    model.fit(X_train_kf, y_train_kf)
    
    # Make predictions
    y_pred_kf = model.predict(X_test_kf)
    
    # Calculate accuracy
    accuracy_kf = accuracy_score(y_test_kf, y_pred_kf)
    
    print(f"\nFold {fold}:")
    print(f"Training indices: {train_index}")
    print(f"Testing indices: {test_index}")
    print(f"Predicted labels: {y_pred_kf}")
    print(f"Actual labels: {y_test_kf}")
    print(f"Accuracy: {accuracy_kf:.2f}")
    
    fold += 1

# Plot the standardized features
plt.figure(figsize=(10, 6))
plt.title('Standardized Features of Iris Dataset')
for i, feature in enumerate(iris.feature_names):
    plt.subplot(2, 2, i + 1)
    plt.hist(X_scaled[:, i], bins=20, alpha=0.7, color='blue')
    plt.title(feature)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot the PCA-transformed version of the Iris dataset
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(pca_df['Principal Component 1'], pca_df['Principal Component 2'], c=pca_df['Target'], cmap='viridis', edgecolor='k', s=50)
legend = ax.legend(*scatter.legend_elements(), title="Classes")
ax.add_artist(legend)
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_title('PCA of Iris Dataset')
plt.show()

# Display PCA results
print("\nPCA Results:")
print(pca_df.head())
