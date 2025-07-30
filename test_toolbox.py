
import asyncio
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

async def main():
    try:
        from toolbox_core import ToolboxClient
    except ImportError:
        print("toolbox-core not found. Installing...")
        install("toolbox-core")
        from toolbox_core import ToolboxClient

    # The server is running on the default port 5000
    async with ToolboxClient("http://127.0.0.1:5000") as client:
        try:
            # First, try to initialize the database
            try:
                init_tool = await client.load_tool("initialize-database")
                await init_tool()
                print("Database initialized.")
            except Exception as e:
                # If the table already exists, we can ignore the error
                if "table hotels already exists" in str(e):
                    print("Database already initialized.")
                    pass
                else:
                    # If it's a different error, we should raise it
                    raise e

            # The tool name is "search-hotels-by-city"
            tool = await client.load_tool("search-hotels-by-city")
            
            # The parameter name is "city"
            result = await tool(city="New York")
            print("Successfully ran the tool. Result:")
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
