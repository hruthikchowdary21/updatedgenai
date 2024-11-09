import csv

# File input: Reading content from a CSV file
with open('Airlines_Flights_Dataset.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    rows = list(csv_reader)  # Read all rows into a list
    print("Content of input.csv:")
    for row in rows:
        print(row)

# File output: Writing content to a new CSV file
with open('output.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(rows)
    print("\nContent has been written to output.csv")