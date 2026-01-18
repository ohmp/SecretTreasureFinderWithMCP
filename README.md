---
title: SecrectDocumentLocker
app_file: app.py
sdk: gradio
sdk_version: 6.3.0
---
# SmolAgents with FastMCP Demo

This project demonstrates a [SmolAgents](https://github.com/huggingface/smolagents) agent interacting with a local [MCP](https://modelcontextprotocol.io/) server created using [FastMCP](https://github.com/jlowin/fastmcp).

## Features

- **MCP Server**: (`mcp_server.py`)
    - Implements a dummy authentication tool.
    - Protects a "treasure" resource (`treasure://secret`) which is only accessible after authentication.
    - Exposes a `read_treasure` tool.
- **Agent**: (`agent.py`)
    - Uses `smolagents.MCPClient` to connect to the local MCP server.
    - Dynamically loads tools from the MCP server.
    - Uses `meta-llama/Llama-4-Scout` model via Hugging Face Inference API.
- **UI**: (`app.py`)
    - Provides a Gradio chat interface for the agent.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    You need a Hugging Face Token to use the Inference API.
    Create a `.env` file in the root directory:
    ```bash
    HF_TOKEN=your_hf_token_here
    ```

## Running Locally

1.  Run the Gradio app:
    ```bash
    python app.py
    ```
2.  Open the link provided in the terminal (usually http://127.0.0.1:7860).
3.  Chat with the agent! Try:
    > "Read the treasure file."
    > (The agent should try, fail, then realize it needs to authenticate. Hint: the password is "open sesame")

## Deploying to Hugging Face Spaces

1.  Create a new Space on Hugging Face (SDK: **Gradio**).
2.  Upload the files:
    - `app.py`
    - `agent.py`
    - `mcp_server.py`
    - `dummy_treasure.txt`
    - `requirements.txt`
3.  Set the `HF_TOKEN` in the Space's **Settings > Variables and secrets** (if not automatically handled, though Spaces usually have access to the token of the owner if configured, but explicit token is safer for specific model access).
4.  The Space should build and run automatically!

## Files

- `mcp_server.py`: The FastMCP server implementation.
- `agent.py`: Agent logic including MCP connection.
- `app.py`: Entry point for Gradio.
- `dummy_treasure.txt`: The protected content.

## Deploying to Hugging Face Spaces

1.  Create a new Space on Hugging Face (SDK: **Gradio**).
2.  Upload the files:
    - `app.py`
    - `agent.py`
    - `mcp_server.py`
    - `dummy_treasure.txt`
    - `requirements.txt`
3.  Set the `HF_TOKEN` in the Space's **Settings > Variables and secrets** (if not automatically handled, though Spaces usually have access to the token of the owner if configured, but explicit token is safer for specific model access).
4.  The Space should build and run automatically!

## Files

- `mcp_server.py`: The FastMCP server implementation.
- `agent.py`: Agent logic including MCP connection.
- `app.py`: Entry point for Gradio.
- `dummy_treasure.txt`: The protected content.

## Deploying to Hugging Face Spaces

```bash
hf upload --repo-type space ohmp/SecrectDocumentLocker . --exclude ".env" ".venv/**" "__pycache__/**" "*.pyc"
```