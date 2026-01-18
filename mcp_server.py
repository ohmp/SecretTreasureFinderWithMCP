from fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("TreasureKeeper")

# Global state for authentication (Mock)
# In a real scenario, this would be session-based or token-based
auth_state = {
    "authenticated": False
}

TREASURE_PATH = os.path.join(os.path.dirname(__file__), "dummy_treasure.txt")

@mcp.tool()
def authenticate(password: str) -> str:
    """
    Authenticate to access the restricted treasure.
    
    Args:
        password: The password to unlock the treasure. Hint: It's 'open sesame'.
    """
    if password.lower() == "open sesame":
        auth_state["authenticated"] = True
        return "Authentication successful! You can now access the treasure."
    else:
        return "Authentication failed. Incorrect password."

def _read_treasure_logic() -> str:
    if not auth_state["authenticated"]:
        return "ACCESS DENIED: You must authenticate first using the 'authenticate' tool."
    
    try:
        with open(TREASURE_PATH, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading treasure: {str(e)}"

@mcp.resource("treasure://secret")
def get_treasure() -> str:
    """
    Get the secret treasure content. Requires authentication first.
    """
    return _read_treasure_logic()

@mcp.tool()
def read_treasure() -> str:
    """
    Read the secret treasure content. Requires authentication first.
    """
    return _read_treasure_logic()

if __name__ == "__main__":
    mcp.run()
