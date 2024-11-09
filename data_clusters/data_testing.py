import numpy as np
import random
from scipy.stats import ttest_ind, chi2_contingency

# 1. Parametric Testing Example: Comparing Healthcare Costs
print("Parametric Testing Example:")
np.random.seed(0)
under_50_costs = np.random.normal(5000, 1500, 100)  # Average cost $5000 with std dev $1500
over_50_costs = np.random.normal(7000, 1800, 100)  # Average cost $7000 with std dev $1800
t_stat, p_value = ttest_ind(under_50_costs, over_50_costs)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
print("\n")

# 2. Non-Parametric Testing Example: Comparing Customer Satisfaction Ratings
print("Non-Parametric Testing Example:")
np.random.seed(1)
plan_a_ratings = np.random.randint(1, 6, 50)  # Ratings between 1 and 5
plan_b_ratings = np.random.randint(1, 6, 50)
sum_a = np.sum(plan_a_ratings)
sum_b = np.sum(plan_b_ratings)
print(f"Sum of Ratings - Plan A: {sum_a}, Plan B: {sum_b}")
print("\n")

# 3. A/B Testing Example: Comparing Sign-up Rates for Emails
print("A/B Testing Example:")
np.random.seed(2)
# Simulating responses (1 = signed up, 0 = did not sign up)
email_a_responses = [random.choice([0, 1]) for _ in range(100)]
email_b_responses = [random.choice([0, 1]) for _ in range(100)]
conversion_rate_a = sum(email_a_responses) / len(email_a_responses)
conversion_rate_b = sum(email_b_responses) / len(email_b_responses)
t_stat_ab, p_value_ab = ttest_ind(email_a_responses, email_b_responses)
print(f"Conversion Rate A: {conversion_rate_a:.2f}, Conversion Rate B: {conversion_rate_b:.2f}")
print(f"T-statistic: {t_stat_ab}, P-value: {p_value_ab}")
print("\n")

# 4. Chi-Square Testing Example: Association Between Chronic Condition and Insurance Plan
print("Chi-Square Testing Example:")
contingency_table = np.array([[50, 80], [30, 60], [20, 30], [40, 50]])
chi2_stat, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-Square Statistic: {chi2_stat}, P-value: {p}")
