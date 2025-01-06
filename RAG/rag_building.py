import schedule
import time
import docx
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import hashlib

# Configuration
doc_path = "C:/Users/hruth/GENAI/RAG/rrr.docx"
db_client = MongoClient("mongodb://localhost:27017/")
db = db_client['text_embeddings']
collection = db['embeddings']
model = SentenceTransformer('all-MiniLM-L6-v2')

# Keep track of the last processed point
last_hash = None

def process_document():
    global last_hash
    doc = docx.Document(doc_path)
    full_text = [para.text for para in doc.paragraphs if para.text.strip()]
    full_text_concat = "\n".join(full_text)
    current_hash = hashlib.sha256(full_text_concat.encode()).hexdigest()

    # Check if the document has changed
    if current_hash == last_hash:
        print("No changes detected.")
        return

    last_hash = current_hash

    # Embed new texts
    new_texts = {text: model.encode([text])[0] for text in full_text}
    existing_texts = {doc['text']: doc['embedding'] for doc in collection.find()}

    # Find new and deleted texts
    new_entries = [text for text in new_texts if text not in existing_texts]
    deleted_entries = [text for text in existing_texts if text not in new_texts]

    # Update MongoDB
    if new_entries:
        new_documents = [{'text': text, 'embedding': new_texts[text].tolist()} for text in new_entries]
        collection.insert_many(new_documents)
        print(f"Inserted {len(new_documents)} new documents.")

    if deleted_entries:
        collection.delete_many({'text': {'$in': deleted_entries}})
        print(f"Deleted {len(deleted_entries)} documents.")

# Schedule to run every 10 seconds
schedule.every(10).seconds.do(process_document)

# Loop to keep the scheduler running
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by the user.")
