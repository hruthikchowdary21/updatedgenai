# Total number of cards in a standard deck
total_cards = 52

# Number of black cards (spades + clubs)
black_cards = 26

# Number of black kings
black_kings = 2

# Probability of picking a black king (P(A))
P_A = black_kings / total_cards

# Probability of picking a black card (P(B))
P_B = black_cards / total_cards

# Function to calculate conditional probability using Bayes' theorem
def bayes_theorem():
    # Probabilities
    P_A = 2 / 52  # Probability of picking a black king
    P_B = 26 / 52  # Probability of picking a black card
    P_B_given_A = 1  # Probability of picking a black card given a black king

    # Applying Bayes' theorem
    P_A_given_B = (P_B_given_A * P_A) / P_B

    return P_A_given_B

# Calculate and print the result
result = bayes_theorem()
print(f"P(A|B) - Probability of picking a black king given that a black card has been picked: {result:.4f}")