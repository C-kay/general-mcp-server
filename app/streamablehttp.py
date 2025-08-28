import os
import sys
from dotenv import load_dotenv
from pydantic_ai.mcp import MCPServerStreamableHTTP
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()
REQUIRED_TOKEN = os.getenv("MCP_TOKEN")

async def main():
    async with MCPServerStreamableHTTP(
        url = "http://127.0.0.1:6274/mcp",
        headers={"Authorization": f"Bearer {REQUIRED_TOKEN}"}
    ) as server :
        tool_list = await server.list_tools()
        for tool in tool_list:
            print(f"Tool name: {tool.name}")

        print("Connected to MCP Server over Streamable HTTP.")

if __name__ == "__main__":
    asyncio.run(main())