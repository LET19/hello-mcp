# server.py
import asyncio
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-mcp")

# 定义一个最简单的工具：echo
@mcp.tool()
async def my_echo(text: str) -> str:
    """Return the same text back."""
    return text

# 定义一个最简单的工具：reverse echo
@mcp.tool()
async def rev_echo(text: str) -> str:
    """Return the reversed text back."""
    return text[::-1]

if __name__ == "__main__":
    # 通过 STDIO 跑起来（MCP 推荐）
    # 注意：不要 print 到 stdout，日志请走 stderr！
    # 见官方“Logging in MCP Servers”与“Best Practices”。
    mcp.run(transport="stdio")
