
# Document Synchronization Script

This Python script continuously monitors changes in a specified Word document and synchronizes its content with a MongoDB database. It uses document embeddings to represent text chunks and updates the database to reflect any additions or deletions in the document content.

## Features

- **Continuous Monitoring**: The script checks the document every 10 seconds for any changes.
- **Change Detection**: Utilizes SHA-256 hashing to detect any modifications in the document.
- **Dynamic Updates**: Only new text chunks are embedded and added to the database, and deletions are removed.
- **Embedding with Sentence Transformers**: Text chunks are converted into embeddings using the `all-MiniLM-L6-v2` model from Sentence Transformers.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.6 or higher
- MongoDB
- Python packages: `pymongo`, `docx`, `schedule`, `sentence-transformers`

## Installation

1. **Install Python Packages**:
   ```bash
   pip install pymongo python-docx schedule sentence-transformers
   ```

2. **MongoDB**:
   Ensure MongoDB is installed and running on your system. The script connects to MongoDB at `mongodb://localhost:27017/`.

## Configuration

Modify the script to point to the correct document path:
```python
doc_path = "C:/Users/hruth/GENAI/RAG/rrr.docx"
```

Ensure the MongoDB URI, database, and collection names match your setup:
```python
db_client = MongoClient("mongodb://localhost:27017/")
db = db_client['text_embeddings']
collection = db['embeddings']
```

## Usage

Run the script using Python:
```bash
python path_to_script.py
```

The script will start monitoring the document and update the database as needed. It runs indefinitely until manually stopped.

## How It Works

1. **Document Reading**: The script reads the Word document and concatenates its content.
2. **Change Detection**: Computes a hash of the content and compares it with the previous hash to detect changes.
3. **Embedding and Updating**: If changes are detected, the script identifies new and deleted text, updates embeddings for new text, and updates the database accordingly.

## Stopping the Script

To stop the script, use the keyboard interrupt:
```bash
Ctrl + C
```

## Notes

- The script assumes that the MongoDB server is running locally and that there is no authentication set up.
- Adjust the MongoDB URI and document path according to your environment.

## License

This script is provided "as is", without warranty of any kind, express or implied. Use at your own risk.
