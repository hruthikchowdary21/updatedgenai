import pandas as pd

# Given data
P_A = 0.05  # Probability of a claim being fraudulent
P_B_given_A = 0.70  # Probability of seeing suspicious features given the claim is fraudulent
P_B_given_not_A = 0.10  # Probability of seeing suspicious features given the claim is not fraudulent
P_not_A = 1 - P_A  # Probability of a claim being genuine

# Calculate P(B)
P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A)

# Calculate P(A|B) using Bayes' theorem
P_A_given_B = (P_B_given_A * P_A) / P_B

# Print the result
print(f"The probability that a claim is fraudulent given that it has suspicious features is: {P_A_given_B:.2%}")

# Example output: The probability that a claim is fraudulent given that it has suspicious features is: 26.92%
