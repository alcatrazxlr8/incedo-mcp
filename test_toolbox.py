import asyncio
import subprocess
import sys
import json

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

            # Get user input for the city
            city_to_search = input("Please enter a city to search for hotels (e.g., New York, Paris): ")

            # The tool name is "search-hotels-by-city"
            tool = await client.load_tool("search-hotels-by-city")
            
            # The parameter name is "city"
            json_result = await tool(city=city_to_search)

            # Parse the JSON string result into a Python list
            result = json.loads(json_result)
            
            print(f"\n--- Search Results for '{city_to_search}' ---")
            if result:
                for hotel in result:
                    print(f"- {hotel['name']}")
            else:
                print("No hotels found.")
            print("------------------------------------")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())