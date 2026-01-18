from smolagents import GradioUI
from agent import create_agent_with_mcp
import os

# Initialize the agent and client
# The client connection stays alive as long as this process is running
agent, client = create_agent_with_mcp()

def main():
    # Create the Gradio UI
    ui = GradioUI(agent)
    # Launch with public link if possible, or just local
    ui.launch()

if __name__ == "__main__":
    main()
