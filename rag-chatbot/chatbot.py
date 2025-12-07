import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
import cohere

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

# --- Constants ---
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


def embed_chunks(chunks, input_type="search_document"):
    """Embeds a list of text chunks using Cohere."""
    response = cohere_client.embed(
        model=EMBED_MODEL,
        input_type=input_type,
        texts=chunks,
    )
    return response.embeddings

def search_for_context(query):
    """Searches for relevant context in Qdrant based on a query."""
    vector = embed_chunks([query], input_type="search_query")[0]
    
    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=5  # Return top 5 most relevant chunks
    )
    
    # Extract the text from the search results
    context = [result.payload["text"] for result in search_result]
    return context

def ask_question(query):
    """Handles a user question by searching for context and generating an answer."""
    context = search_for_context(query)
    
    # Format the documents for the chat model
    documents = [{"title": f"Source {i+1}", "snippet": doc} for i, doc in enumerate(context)]
    
    # Generate a response using the retrieved context
    response = cohere_client.chat(
        message=query,
        documents=documents,
        model="command",
        preamble="You are an expert AI assistant answering questions based on the provided book content. Your goal is to provide clear and concise answers. If the answer cannot be found in the provided context, state that clearly."
    )
    
    return response.text
