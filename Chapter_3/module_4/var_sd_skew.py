import numpy as np
from scipy.stats import skew, mode
import matplotlib.pyplot as plt

# Dataset
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Mode
mode_result = mode(data)
if mode_result.count[0] > 0:
    mode_value = mode_result.mode[0]  # Get the mode value
    mode_count = mode_result.count[0]  # Get the count of the mode
else:
    mode_value = None
    mode_count = 0

# Variance
variance = np.var(data, ddof=1)  # ddof=1 for sample variance

# Standard Deviation
std_deviation = np.std(data, ddof=1)

# Skewness
skewness = skew(data)

# Print the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode_value} (Count: {mode_count})")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"Skewness: {skewness}")

# Plotting the data
plt.figure(figsize=(12, 8))

# Histogram
plt.subplot(2, 2, 1)
plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean:.2f}')
plt.axvline(median, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')
plt.axvline(mode_value, color='orange', linestyle='dashed', linewidth=1, label=f'Mode: {mode_value}')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Box Plot
plt.subplot(2, 2, 2)
plt.boxplot(data, vert=False)
plt.title('Box Plot of Data')
plt.xlabel('Value')

# Skewness Plot
plt.subplot(2, 2, 3)
plt.plot(data, np.zeros_like(data), 'o', label='Data Points')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean:.2f}')
plt.axvline(median, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')
plt.title('Data Points with Mean and Median')
plt.xlabel('Value')
plt.yticks([])
plt.legend()

# Show plots
plt.tight_layout()
plt.show()
