from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import sys

print("web.py: Starting script execution.")
try:
    from chatbot import ask_question
    print("web.py: Successfully imported ask_question from chatbot.py.")
except ImportError as e:
    print(f"web.py: ERROR importing ask_question from chatbot.py: {e}", file=sys.stderr)
    sys.exit(1) # Exit if critical import fails

class Query(BaseModel):
    query: str

print("web.py: Initializing FastAPI app.")
app = FastAPI()

# Add CORS middleware
print("web.py: Adding CORS middleware.")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows requests from Docusaurus dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(query: Query):
    print(f"web.py: Received request for query: {query.query}")
    try:
        answer = ask_question(query.query)
        print("web.py: Successfully got answer from ask_question.")
        return {"answer": answer}
    except Exception as e:
        print(f"web.py: ERROR calling ask_question: {e}", file=sys.stderr)
        # Optionally, return an error message to the client
        return {"answer": "Sorry, an internal server error occurred."}

if __name__ == "__main__":
    print("web.py: Running uvicorn server.")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print("web.py: Uvicorn server stopped.")