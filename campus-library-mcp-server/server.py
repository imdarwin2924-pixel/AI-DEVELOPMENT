import asyncio

from mcp.server import MCPServer


# Create the Campus Library MCP Server
mcp = MCPServer("Campus Library MCP Server")


async def main() -> None:
    """Run the Campus Library MCP server."""
    await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())