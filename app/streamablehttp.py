from pydantic_ai.mcp import MCPServerStreamableHTTP
import asyncio

async def main():
    async with MCPServerStreamableHTTP(
        url = "http://0.0.0.0:10000/mcp",
    ) as server :
        tool_list = await server.list_tools()
        for tool in tool_list:
            print(f"Tool name: {tool.name}")

        print("Connected to MCP Server over Streamable HTTP.")

if __name__ == "__main__":
    asyncio.run(main())