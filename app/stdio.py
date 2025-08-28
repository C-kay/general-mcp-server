from pydantic_ai.mcp import MCPServerStdio
import asyncio, sys, os

# Resolve server.py path & working directory
HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(HERE, "server.py")

async def main():
    async with MCPServerStdio(
        command=sys.executable,                  # run with the *same* Python interpreter
        args=["-u", SERVER],                     # -u = unbuffered stdio (important on Windows)
        cwd=HERE,
    ) as server :
        tool_list = await server.list_tools()
        for tool in tool_list:
            print(f"Tool name: {tool.name}")

        print("Starting MCP Server...")


if __name__ == "__main__":
    asyncio.run(main())