import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: Load the dataset from a CSV file
# Make sure to specify the correct path to your CSV file
df = pd.read_csv('C:/Users/hruth/Documents/diabetes_ND.csv')

# Step 2: Select the relevant column for the normal distribution calculation
# Assuming 'BMI' is the name of the column you want to use
data = df['BMI'].values

# Step 3: Calculate mean and median
mean = np.mean(data)
median = np.median(data)

# Print mean and median
print(f"Mean: {mean:.4f}")
print(f"Median: {median:.4f}")

# Step 4: Generate x values for the distribution
std_dev = np.std(data)  # Calculate standard deviation
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

# Step 5: Calculate the PDF for the normal distribution
pdf = norm.pdf(x, mean, std_dev)

# Step 6: Plot the normal distribution and the data histogram
plt.plot(x, pdf, label='Fitted Normal Distribution', color='blue')
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data Histogram')
plt.title('Normal Distribution of the Dataset')
plt.xlabel('X values')
plt.ylabel('Density')
plt.legend()
plt.show()
