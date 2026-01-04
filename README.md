# AI Dev Tools: MCP Server (Homework 3)

This repository contains the solution for **Homework 3** of the DataTalks.Club [AI Dev Tools Course](https://courses.datatalks.club/ai-dev-tools-2025/homework/hw3).

It implements a **Model Context Protocol (MCP)** server using `fastmcp` and includes scripts for web scraping and documentation search (RAG).

## 🚀 Project Overview

The goal of this project is to build a custom MCP server that provides tools for an AI assistant. The implemented tools include:
* **Math Tool:** Basic addition (sanity check).
* **Web Scraper:** Fetches markdown-formatted content from any URL using the Jina Reader API.
* **Documentation Search:** Indexes and searches local documentation using `minsearch`.

## 🛠️ Environment Setup

This project is configured to run in a **VS Code Dev Container**. This ensures a consistent environment with Python 3.12 and `uv` pre-installed.

### Prerequisites
* Docker Desktop
* VS Code
* [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Installation
1.  Clone this repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/mcp-homework.git](https://github.com/YOUR_USERNAME/mcp-homework.git)
    cd mcp-homework
    ```
2.  Open the folder in **VS Code**.
3.  When prompted, click **"Reopen in Container"** (or press `F1` and select *Dev Containers: Reopen in Container*).
4.  Wait for the container to build. Once inside, install dependencies:
    ```bash
    uv sync
    ```

## 📂 Files & Scripts

| File | Description |
| :--- | :--- |
| `main.py` | The core MCP server. defines the `add` and `scrape_page` tools. |
| `search.py` | (Question 5) A script that downloads documentation, indexes it, and searches for "demo". |
| `solve_q4.py` | (Question 4) A script that uses the scrape logic to count the word "data" on a website. |
| `test.py` | A simple unit test for the `scrape_page` functionality. |
| `.devcontainer/` | Configuration files for the Docker development environment. |

## 💻 Usage

### 1. Running the MCP Server
To start the server (for use with an MCP client like Claude Desktop or Inspector):
```bash
uv run main.py
```
### 2. Running Homework Solutions
You can run the specific scripts created for the homework questions directly:

#### Question 4 (Scrape & Count):
```bash
uv run solve_q4.py
```
#### Question 5 (Search/RAG):
```bash
uv run search.py
```

### 3. Testing the Tools
To verify the scraping logic without running the full server:
```bash
uv run test.py
```

## 📚 Technologies Used
* [FastMCP](https://github.com/jlowin/fastmcp): For building the MCP server.
* [uv](https://github.com/astral-sh/uv): For fast Python package management.
* [Minsearch](https://github.com/alexeygrigorev/minsearch): For simple text indexing and search.
* [Jina Reader](https://jina.ai/reader): For converting web pages to LLM-friendly markdown.