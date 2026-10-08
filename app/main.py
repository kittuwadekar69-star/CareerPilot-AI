from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import chat
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="CareerPilot AI",
    description="AI-powered project and placement guidance assistant",
    version="1.0.0"
)

#files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/ui")
def frontend():
    return FileResponse("app/static/index.html")


# Store conversation history in memory
conversations = {}

# Keep the latest 10 messages for context management
MAX_MESSAGES = 10


SYSTEM_PROMPT = """
You are CareerPilot AI, an intelligent project and placement
guidance assistant for computer science students.

Help students with:

- Project ideas and project planning
- Software development
- Coding and debugging
- Resume and LinkedIn improvement
- Technical interviews
- Aptitude preparation
- Group discussions
- Career and placement guidance

Give practical, structured and student-friendly answers.

Prefer realistic projects that students can actually build.
When explaining technical concepts, use simple examples.
When giving project ideas, mention useful technologies and
how the project can strengthen a software developer resume.
"""


class ChatRequest(BaseModel):
    conversation_id: str
    message: str


@app.get("/")
def home():
    return {
        "message": "CareerPilot AI API is running!"
    }


@app.post("/chat")
def chat_endpoint(request: ChatRequest):

    try:
        # Create a new conversation if it doesn't exist
        if request.conversation_id not in conversations:
            conversations[request.conversation_id] = []

        history = conversations[request.conversation_id]

        # Add the user's message
        history.append({
            "role": "user",
            "content": request.message
        })

        # Context-window management:
        # keep only the latest 10 messages
        recent_history = history[-MAX_MESSAGES:]

        # System prompt + recent conversation
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + recent_history

        # Call local Ollama model
        response = chat(
            model="qwen3:0.6b",
            messages=messages
        )

        assistant_reply = response.message.content

        # Save assistant response to conversation history
        history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        return {
            "conversation_id": request.conversation_id,
            "reply": assistant_reply,
            "messages_in_memory": len(history)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Local LLM error: {str(e)}"
        )