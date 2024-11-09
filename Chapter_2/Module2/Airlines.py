import pandas as pd
import networkx as nx

# Load the dataset
try:
    flights_data = pd.read_csv(r'C:/Users/hruth/GENAI/Airlines_Flights_Dataset.csv')
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")
    exit()

# Create a directed graph
flight_graph = nx.DiGraph()

# Add edges from the dataset
for index, row in flights_data.iterrows():
    flight_graph.add_edge(row['Start Airport'], row['Destination Airport'], airline=row['Airline'], flight_number=row['Flight number'])

# Define the source and target cities
source_city = 'City 1'
target_city = 'City 20'

# Find the shortest path based on the fewest hops
try:
    shortest_path = nx.shortest_path(flight_graph, source=source_city, target=target_city)
    shortest_path_length = len(shortest_path) - 1  # Number of flights is nodes - 1
except nx.NetworkXNoPath:
    shortest_path = None
    shortest_path_length = None
except nx.NodeNotFound:
    print(f"One of the cities '{source_city}' or '{target_city}' does not exist in the graph.")
    exit()

# Find all possible paths between the two cities
try:
    all_paths = list(nx.all_simple_paths(flight_graph, source=source_city, target=target_city))
except nx.NetworkXNoPath:
    all_paths = []

# Output results
print("Shortest Path:", shortest_path)
print("Shortest Path Length (hops):", shortest_path_length)
print("All Paths:", all_paths[:10])  # Print only the first 10 paths to avoid excessive output
