from .server import serve


def main():
    """MCP Math Server - Math functionality for MCP"""
    import asyncio

    asyncio.run(serve())


if __name__ == "__main__":
    main()
