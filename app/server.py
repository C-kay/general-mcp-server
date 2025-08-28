import os, sys
import requests
import uvicorn
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.middleware import BearerAuthASGIMiddleware

load_dotenv()
REQUIRED_TOKEN = os.getenv("MCP_TOKEN")
if not REQUIRED_TOKEN:
    raise RuntimeError("MCP_TOKEN is not set in environment/.env")

# ---- MCP Server & Tools ----
mcp = FastMCP("General MCP Server")

@mcp.tool()
def get_weather(city: str) -> str:
    return requests.get(f"https://wttr.in/{city}").text

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

# Get the MCP Streamable HTTP ASGI app and wrap it
inner_app = mcp.streamable_http_app()
app = BearerAuthASGIMiddleware(inner_app, REQUIRED_TOKEN)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)