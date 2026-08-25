import asyncio

from mcp.server import MCPServer

from database import DATABASE_PATH


# Create the Campus Library MCP Server
mcp = MCPServer("Campus Library MCP Server")


@mcp.tool()
async def search_book(query: str) -> list[dict]:
    """
    Search the campus library catalog by title, author, ISBN, or category.

    Args:
        query: Text to search for in the library catalog.

    Returns:
        A list of matching books with availability information.
    """
    import sqlite3

    search_term = query.strip()

    if not search_term:
        return []

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    pattern = f"%{search_term}%"

    cursor.execute(
        """
        SELECT
            id,
            title,
            author,
            isbn,
            category,
            total_copies,
            available_copies
        FROM books
        WHERE title LIKE ?
           OR author LIKE ?
           OR isbn LIKE ?
           OR category LIKE ?
        ORDER BY title
        """,
        (pattern, pattern, pattern, pattern),
    )

    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]


async def main() -> None:
    """Run the Campus Library MCP server."""
    await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())