from pydantic_ai.mcp import MCPServerSSE
import asyncio

async def main():
    async with MCPServerSSE(
        url = "http://127.0.0.1:8000/sse",
    ) as server :
        tool_list = await server.list_tools()
        for tool in tool_list:
            print(f"Tool name: {tool.name}")
        
        print("Connected to MCP Server over SSE.")

if __name__ == "__main__":
    asyncio.run(main())