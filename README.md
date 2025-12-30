# Kilo + SearxNG + Local LLM Setup

Goal:  
A local, privacy-respecting AI workflow for coding and planning using:

- Kilo (agent orchestration)
- Ollama (local LLM)
- SearxNG (local search engine)

All fully local, no cloud APIs required.

![Workflow Diagram](/docs/assets/workflow.png)
---

## Repository Layout

```
kilo-local-ai/
├── scripts/
│   ├── start_agents.py
│   └── query_searxng.py
├── docker/
│   └── searxng/
│       ├── docker-compose.yml
│       └── settings.yml
├── .sample.env
├── .env                # not committed
├── README.md
```

---

## Prerequisites

- VS Code (latest)
- Python 3.11+
- Docker Desktop
- Ollama
- Internet connection (for first model pull)

Install Python dependencies:

python -m pip install requests

---

## 1. SearxNG Setup

1. Copy `.sample.env` → `.env` and fill in a random 32-character secret:
    ```
    SEARX_SECRET_KEY=your_random_32_char_secret_here
    ```

2. Start SearxNG (from script or manually):
   ```
   python scripts/start_agents.py
   ```

Verify:
```
curl "http://localhost:18080/search?q=test&format=json"
```
---

## 2. Ollama Setup

Pull recommended model:

    ollama pull qwen3:4b

Start Ollama (if not already running):

    python scripts/start_agents.py

---

## 3. Kilo Setup

1. Open VS Code  
2. Install Kilo extension  
3. Configure provider:
   - API Provider: Ollama  
   - Base URL: http://localhost:11434  
   - Model: qwen3:4b  
   - Context size: 32000 (adjust carefully for RAM)

---

## 4. Start Agents

    python scripts/start_agents.py

- Starts Ollama (if not running)  
- Starts SearxNG Docker container  
- Prints health summary  

Press `Ctrl+C` to stop SearxNG & Ollama.

---

## 5. Using SearxNG with Kilo

In Kilo Architect/Code:

> Look up "{SEARCH_TERM_HERE}" using "Projects\kilo-local-ai\scripts\query_searxng.py"

This allows the agent to search locally and use results in planning or coding.

---

## 6. Planned Features

### 6.1 VS Code Extension (Auto-Start Agents)

Status: Planned / TODO

- Automatically run `start_agents.py` when VS Code starts  
- Use a lock file for safety  
- Optional auto-stop on exit  

### 6.2 MCP Server Support for SearxNG

Status: Planned / TODO

- Use an MCP (Model Context Protocol) server to expose SearxNG as a native tool in Kilo Code  
- Allows the agent to call the search tool directly, with structured JSON results  
- Will replace or augment the current `query_searxng.py` script for more robust tool integration  
- Configuration will live in `.kilocode/mcp.json` or global MCP settings

---

## 7. Kilo VS Code

> Did you know you can have Kilo Code on the right side of VS Code? Gives you easy access to Kilo Code and your file browser at the same time. 
>
>Just right click on the Kilo Code icon and say "Move to" --> "Secondary side bar"