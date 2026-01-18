from smolagents import CodeAgent, InferenceClientModel, MCPClient
from mcp import StdioServerParameters
import os

def create_agent_with_mcp():
    # Path to server
    server_path = os.path.join(os.path.dirname(__file__), "mcp_server.py")
    
    # Parameters
    params = StdioServerParameters(
        command="python",
        args=[server_path],
        env=os.environ.copy()
    )
    
    # Initialize Client
    # We create the client but need to manage its lifecycle.
    # For a simple demo script or Gradio app, we can keep the client content_manager logic in the caller 
    # OR just instantiate it and manualy disconnect later.
    client = MCPClient(params, structured_output=True)
    
    # The tools are now available in client.get_tools()
    # Note: connect() is called inside __init__ of MCPClient
    mcp_tools = client.get_tools()
    print(f"Debug: mcp_tools type: {type(mcp_tools)}")
    if mcp_tools:
        print(f"Debug: first tool type: {type(mcp_tools[0])}")
        print(f"Debug: mcp_tools: {mcp_tools}")
    
    # Using InferenceClientModel with Llama 4 Scout
    model = InferenceClientModel(
        model_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    )
    
    agent = CodeAgent(
        tools=mcp_tools,
        model=model,
        max_steps=5, # Limit steps to avoid excessive token usage
    )
    return agent, client

if __name__ == "__main__":
    try:
        agent, client = create_agent_with_mcp()
        tools_list = agent.tools.values() if isinstance(agent.tools, dict) else agent.tools
        print("Agent created with tools:", [t.name for t in tools_list])
        
        # Test run
        print("Running agent test...")
        response = agent.run("Please authenticate with 'open sesame' and then read the treasure.")
        print("Agent Response:", response)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'client' in locals():
            client.disconnect()
