import numpy as np



# Define the adjacency matrix for the DVD interactions
# Each row and column represents a DVD, and the value represents the interaction strength
# For simplicity, assume we have 4 DVDs and the matrix is symmetric
adjacency_matrix = np.array([
    [0, 1, 1, 0],  # DVD 1 is linked to DVD 2 and DVD 3
    [0, 0, 0, 0],  # DVD 2 is linked to DVD 1, DVD 3, and DVD 4
    [1, 1, 0, 1],  # DVD 3 is linked to DVD 1, DVD 2, and DVD 4
    [0, 1, 1, 0]   # DVD 4 is linked to DVD 2 and DVD 3
])

# Number of DVDs
n = adjacency_matrix.shape[0]

# Create a stochastic matrix by normalizing the adjacency matrix
stochastic_matrix = adjacency_matrix / adjacency_matrix.sum(axis=0)

# Damping factor
damping_factor = 0.85

# Create the PageRank matrix
pagerank_matrix = damping_factor * stochastic_matrix + (1 - damping_factor) / n * np.ones((n, n))

# Initialize the PageRank vector
pagerank_vector = np.ones(n) / n

# Power iteration method to compute the principal eigenvector
for _ in range(100):  # Iterate 100 times for convergence
    pagerank_vector = pagerank_matrix @ pagerank_vector

# Normalize the PageRank vector
pagerank_vector /= pagerank_vector.sum()

# Print the PageRank scores for each DVD
for i, score in enumerate(pagerank_vector, start=1):
    print(f"DVD {i} PageRank Score: {score:.5f}")
