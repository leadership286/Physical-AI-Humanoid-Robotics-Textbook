import os
import glob
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
import cohere
import argparse

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

# --- Constants ---
# Path to the book's documentation files
DOCS_PATH = "../1-docusaurus-book/docs"
# Qdrant collection name
COLLECTION_NAME = "humanoid_ai_book_v2"
# Cohere embedding model
EMBED_MODEL = "embed-english-v3.0"

# --- API Clients ---
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

if not COHERE_API_KEY or not QDRANT_URL or not QDRANT_API_KEY:
    raise RuntimeError("Missing API keys in .env file. Please check your configuration.")

cohere_client = cohere.Client(COHERE_API_KEY)
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)


# -----------------------------
# Helper functions for ingestion
# -----------------------------

def get_all_doc_paths(directory):
    """Finds all markdown files in the specified directory."""
    return glob.glob(f"{directory}/**/*.md", recursive=True)

def extract_text_from_file(path):
    """Reads the text content from a file."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_text(text, max_chars=1200):
    """Splits text into chunks of a specified max size."""
    chunks = []
    current_pos = 0
    while current_pos < len(text):
        end_pos = current_pos + max_chars
        # Ensure we don't split in the middle of a word
        if end_pos < len(text):
            end_pos = text.rfind(". ", current_pos, end_pos) + 1
            if end_pos == 0:  # If no period is found, just split at max_chars
                end_pos = current_pos + max_chars
        
        chunks.append(text[current_pos:end_pos])
        current_pos = end_pos
    return chunks

def embed_chunks(chunks, input_type="search_document"):
    """Embeds a list of text chunks using Cohere."""
    response = cohere_client.embed(
        model=EMBED_MODEL,
        input_type=input_type,
        texts=chunks,
    )
    return response.embeddings

def create_and_upload_collection(docs):
    """Creates a Qdrant collection and uploads the document chunks."""
    print(f"Recreating Qdrant collection: {COLLECTION_NAME} ...")
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE)
    )

    chunk_id = 0
    for doc_path in docs:
        print(f"Processing: {doc_path}")
        text = extract_text_from_file(doc_path)
        if not text:
            print(f"[WARNING] No text extracted from: {doc_path}")
            continue

        chunks = chunk_text(text)
        print(f"  - Created {len(chunks)} chunks.")
        
        embeddings = embed_chunks(chunks)
        
        points = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            points.append(models.PointStruct(
                id=chunk_id + i,
                vector=embedding,
                payload={"source": doc_path, "text": chunk}
            ))
        
        if points:
            qdrant_client.upsert(
                collection_name=COLLECTION_NAME,
                points=points,
                wait=True
            )
            print(f"  - Uploaded {len(points)} points to Qdrant.")
        
        chunk_id += len(chunks)

    print("\n✔️ Ingestion completed!")
    print(f"Total chunks stored: {chunk_id}")

# -----------------------------
# Main ingestion pipeline
# -----------------------------

def ingest_docs():
    """Finds all documents, processes them, and uploads them to Qdrant."""
    doc_paths = get_all_doc_paths(DOCS_PATH)
    print(f"Found {len(doc_paths)} documents to ingest.")
    if not doc_paths:
        print("No documents found. Please check the DOCS_PATH.")
        return

    create_and_upload_collection(doc_paths)


# -----------------------------
# Main execution
# -----------------------------

def main():
    """Main function to handle command-line arguments for ingestion or chat."""
    parser = argparse.ArgumentParser(description="RAG Chatbot for your book.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Sub-parser for the 'ingest' command
    ingest_parser = subparsers.add_parser("ingest", help="Ingest documents into the vector database.")
    
    args = parser.parse_args()
    
    if args.command == "ingest":
        ingest_docs()

if __name__ == "__main__":
    main()