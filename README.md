# CareerPilot AI

CareerPilot AI is an AI-powered project and placement guidance assistant designed for computer science students.

It provides conversational assistance for:

- Project ideas and planning
- Software development
- Coding and debugging
- Resume improvement
- Technical interview preparation
- Aptitude preparation
- Group discussions
- Career and placement guidance

## Features

### 1. Conversational AI

CareerPilot AI uses a locally hosted Qwen3 language model through Ollama.

### 2. Multi-Turn Conversations

Each conversation is associated with a unique `conversation_id`, allowing the assistant to maintain context across multiple user messages.

### 3. Context Window Management

The application keeps the most recent 10 messages from a conversation to prevent unlimited context growth.

### 4. Custom System Prompt

CareerPilot AI uses a custom system prompt defining its role as a project and placement guidance assistant.

### 5. REST API

The backend is implemented using FastAPI.

### 6. Web Interface

A simple responsive chat interface allows users to interact with CareerPilot AI directly through a browser.

## Technology Stack

- Python
- FastAPI
- Ollama
- Qwen3 0.6B
- HTML
- CSS
- JavaScript
- Pydantic

## Architecture

```text
User
  |
  v
Web Interface
  |
  v
FastAPI /chat Endpoint
  |
  v
Conversation Manager
  |
  v
Last 10 Messages
  |
  v
CareerPilot System Prompt
  |
  v
Ollama
  |
  v
Qwen3 0.6B
  |
  v
AI Response