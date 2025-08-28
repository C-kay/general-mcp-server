from mcp.server.fastmcp import FastMCP
import requests


mcp = FastMCP("Weather Server", host="0.0.0.0", port=10000)


@mcp.tool()
def get_weather(city: str)-> str:
    """Fetch weather information for a specific city."""
    endpoint = "https://wttr.in"
    response = requests.get(f"{endpoint}/{city}")
    return response.text


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    #mcp.run()
    mcp.run(transport="sse")