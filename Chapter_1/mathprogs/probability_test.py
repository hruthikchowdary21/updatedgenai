import sympy  # Import the sympy library for prime number generation

def generate_set_b(n):
    """Generate the first n odd numbers."""
    # List comprehension to generate the first n odd numbers
    return [2 * i + 1 for i in range(n)]

def generate_set_a(upper_bound):
    """Generate all prime numbers up to the given upper bound."""
    # Use sympy's primerange function to generate primes up to upper_bound
    return list(sympy.primerange(1, upper_bound + 1))

def calculate_probability(set_a, set_b):
    """Calculate the probability of a number being in set A given that it is in set B."""
    # Find the intersection of set A and set B
    intersection = set(set_a).intersection(set(set_b))
    # Calculate the probability as the ratio of the intersection size to the size of set B
    return len(intersection) / len(set_b)

# Generate set B (first 1000 odd numbers)
set_b = generate_set_b(1000)

# The upper bound for set A is the maximum value in set B
upper_bound = max(set_b)

# Generate set A (prime numbers up to the upper bound of set B)
set_a = generate_set_a(upper_bound)

# Calculate the probability
probability = calculate_probability(set_a, set_b)

# Print the result
print(f"The probability of a number being in set A given that it is in set B is: {probability:.4f}")