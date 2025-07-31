# Experimenting with Google's MCP Toolbox for Databases

This project is a hands-on experiment to understand and test the functionality of **Google's MCP (Model Context Protocol) Toolbox for Databases**.

## Overview

The primary goal is to set up a minimal, working example of the MCP Toolbox. This involves:

1.  Running the toolbox server.
2.  Configuring the server with a simple, in-memory database.
3.  Creating a client application to interact with the server and execute tools.

## Current Status

-   The `genai-toolbox` directory contains the pre-compiled binary for the MCP Toolbox server (`toolbox.exe`) and its configuration file (`tools.yaml`).
-   The `tools.yaml` file defines an in-memory SQLite database with a `hotels` table and two tools:
    -   `initialize-database`: Creates the `hotels` table and populates it with sample data.
    -   `search-hotels-by-city`: Queries the `hotels` table for hotels in a specific city.
-   The `test_toolbox.py` script is an interactive Python client that connects to the server, initializes the database, and prompts the user for a city to search for. It then prints the results of the query.

## How to Run

1.  **Start the MCP Toolbox Server**:

    Open a terminal, navigate to the `genai-toolbox` directory, and run the following command:

    ```shell
    curl -o toolbox.exe https://storage.googleapis.com/genai-toolbox/v0.10.0/windows/amd64/toolbox.exe ## in "mcp-toolbox"

    .\toolbox.exe --tools-file tools.yaml
    ```

2.  **Run the Python Test Script**:

    Open a second terminal in the project root and run the following command:

    ```shell
    python test_toolbox.py
    ```

    The script will connect to the server, initialize the database (if needed), and print the results of the test query.
