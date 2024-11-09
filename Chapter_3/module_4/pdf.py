import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate normally distributed data
date = np.random.normal(90, 7, 2000)

# Plot histogram
plt.hist(date, bins=30, edgecolor='black')
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Calculate summary statistics
mean = np.mean(date)
median = np.median(date)
variance = np.var(date)
skewness = stats.skew(date)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Skewness: {skewness}")

# Perform Shapiro-Wilk normality test
shapiro_test = stats.shapiro(date)
print(f"Shapiro-Wilk Test p-value: {shapiro_test.pvalue}")
