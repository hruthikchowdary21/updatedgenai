import os

# Specify the full path of the text file
file_path = 'C:/Users/hruth/Downloads/sample1.txt'

try:
    # Attempt to open and read the content of the text file
    with open(file_path, 'r') as file:
        content = file.read()  # Reads the entire content of the file
        print("Content of the text file:")
        print(content)
        
        # Split the content into paragraphs
        paragraphs = content.split('\n\n')  # Assuming paragraphs are separated by double newlines
        
        # Save each paragraph into a separate text file
        for i, paragraph in enumerate(paragraphs, start=1):
            paragraph_file_path = f'C:/Users/hruth/Downloads/paragraph_{i}.txt'
            with open(paragraph_file_path, 'w') as paragraph_file:
                paragraph_file.write(paragraph)
            print(f"Paragraph {i} saved to '{paragraph_file_path}'")
except FileNotFoundError:
    # If the file is not found, print an error message
    print("File not found. Creating an empty file.")
    
    # Create an empty file at the specified path
    with open(file_path, 'w') as file:
        pass  # 'pass' is used to create an empty file
    print(f"An empty file has been created at '{file_path}'.")
