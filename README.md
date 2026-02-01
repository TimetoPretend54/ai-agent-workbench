# Coding Agent + Metasearch Engine + LLM

<p align="center">
    <img src="./docs/assets/ai-agent-workbench.gif" width="90%"/><br>
</p>

## Goal:
A local, privacy-respecting AI workflow for coding and planning using:

- Coding Agent (One of the following)
  - [Kilo](https://github.com/Kilo-Org/kilocode)
  - [Roo Code](https://github.com/RooCodeInc/Roo-Code)
  - [Cline](https://github.com/cline/cline)
- LLM (One of the following)
  - [Ollama](https://github.com/ollama/ollama)
  - [Qwen Code](https://github.com/QwenLM/qwen-code)
- Metasearch Engine
  - [SearxNG](https://github.com/searxng/searxng)

All fully local, no cloud APIs required.

## Workflow
![Workflow Diagram](/docs/assets/workflow.png)
---

## Repository Layout

```
ai-agent-workbench/
├── .kilocode/
│   ├── skills/                           # Agent skills (see global setup below)
│   ├── workflows/                        # Agent workflows (see global setup below)
│   ├── rules/                            # Custom rules for agent behavior and permissions
│   └── system/                           # System components
│       ├── scripts/                      # Scripts accessible from any project
│       │   ├── start_searxng_agents.py   # Starts SearXNG services
│       │   ├── query_searxng.py          # Queries SearXNG search engine
│       │   └── ollama/
│       │       └── start_agents.py       # Starts Ollama services
│       └── docker/                       # Docker configurations
│           └── searxng/
│               ├── docker-compose.yml
│               └── settings.yml
├── .sample.env
├── .env                                  # Not committed
└── README.md
```

## Global Setup (~/.kilocode/)
For global setup instructions (symlink setup for cross-project access), see [.kilocode/README.md#global-system-setup](/.kilocode/README.md#global-system-setup).

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

## Local Hardware Requirements (Ollama + Kilo)

Kilo can run entirely on **local LLMs via Ollama**, but coding agents place **much higher demands** on hardware than simple chat models due to large context windows, planning loops, and tool usage.

### Quick Summary

* **GPU VRAM is the main bottleneck**
* Coding agents work best with **15–30B models**
* Large context (16k–32k+) dramatically increases memory usage
* CPU-only setups are technically possible but **too slow for interactive use**

### Recommended Baseline

| Component | Minimum      | Good Experience |
| --------- | ------------ | --------------- |
| GPU       | 8–16 GB VRAM | **24 GB+ VRAM** |
| RAM       | 32 GB        | **64 GB+**      |
| CPU       | 6–8 cores    | 8–16 cores      |
| Storage   | 500 GB SSD   | 1–2 TB NVMe     |

### What This Means in Practice

* **8–16 GB GPUs** → small models (3–7B), limited agent reliability
* **24 GB GPUs** → usable 15–30B models with tool use
* **48 GB+ GPUs** → large context, faster planning, smoother agents

> ⚠️ For recommended models like `qwen3-coder:30B`, a **24 GB GPU is strongly recommended**. Smaller GPUs may fall back to CPU and become unusably slow.

> 💡 **Don't meet these requirements?** Consider using hosted LLMs like Qwen Code (Section 2b) which can provide better performance without local hardware constraints. This project supports both local and hosted options.

---

## 1. SearxNG Setup

1. Copy `.sample.env` → `.env` and fill in a random 32-character secret:
    ```
    SEARX_SECRET_KEY=your_random_32_char_secret_here
    ```
---
## 2. LLM Setup (Local or Hosted)

You have **two options** for the coding agent LLM:

---

### 2a. Local LLM: Ollama

#### One-Time Setup

1. Pull the recommended model:

        ollama pull qwen3:4b
#### Optional Setup (everytime)

1. Manually start Ollama & SearXNG (if not already running):

        python .kilocode/system/scripts/ollama/start_agents.py

- The script starts Ollama and SearxNG (Docker)
- Health summary will indicate both are running

**Automatic Alternative:**

- Services will be automatically started when needed by the query script
- No manual setup required - the system handles startup automatically

**Notes:**

- Ollama is fully local, private, and no cloud API is needed
- Memory usage scales with model size and context
- Default context: 8192, can increase up to 32000 (adjust for RAM)


---

### 2b. Hosted LLM: Qwen Code (Free, OAuth)

GitHub: https://github.com/QwenLM/qwen-code

#### One-Time Setup

1. Install Qwen Code CLI globally:

        npm install -g @qwen-code/cli
2. Start the CLI interactively:

        qwen
3. Authenticate via OAuth inside the CLI session:
        
        /auth # start OAuth login

   - A browser will open  
   - Log in with your free **qwen.ai account**  
   - Credentials are cached locally  

✅ Only needs to be done **once**.
#### Optional Setup (everytime)

1. Manually start SearXNG (if not already running):

        python .kilocode\system\scripts\start_searxng_agents.py
    - **NOTE:** Make sure Docker is running on the local machine

**Automatic Alternative:**

- SearXNG will be automatically started when needed by the query script
- No manual setup required - the system handles startup automatically

---
## 3. Coding Agent Setup

1. Open VS Code  
2. Install `Kilo` (or Other Coding Agent) extension
   1. `Cline`
   2. `Code Roo`
3. Command Palette (`Ctrl+Shift+P`) -> `Kilo: Select Provider`
   1. Ollama (local)
      - API Provider: Ollama  
      - Base URL: http://localhost:11434 
      - Model: qwen3:4b (or other model downloaded)
      - Context size: 32000 (adjust carefully for RAM)
   2. Qwen Code
      - API Provider: Qwen Code  
      - Base URL: NA
      - Model: `qwen3-coder-plus` (or `qwen3-coder-flash`)   
      - Context size: NA
      - Usage: Prompt Kilo normally — free tier ~2,000 requests/day, 60 requests/min.

---

## 4. Using SearXNG w/ Coding Agent

#### [internet-search-searxng skill](/.kilocode/skills/internet-search-searxng/SKILL.md/)
- Search using SearXNG and use results in planning or coding

#### [internet-search-searxng workflow](/.kilocode/workflows/internet-search-searxng.md/)
- Manual workflow to access the same functionality as the skill (since skills cannot be manually executed yet)
---
## 5. Planned Features

### 5.1 VS Code Extension (Auto-Start Agents)

Status: Planned / TODO

- Automatically run `start_agents.py` when VS Code starts  
- Use a lock file for safety  
- Optional auto-stop on exit  

### 5.2 MCP Server Support for SearxNG

Status: Planned / TODO

- Use an MCP (Model Context Protocol) server to expose SearxNG as a native tool in Kilo Code  
- Allows the agent to call the search tool directly, with structured JSON results  
- Will replace or augment the current `query_searxng.py` script for more robust tool integration  
- Configuration will live in `.kilocode/mcp.json` or global MCP settings

---

## 6. Kilo VS Code

> Did you know you can have Kilo Code on the right side of VS Code? Gives you easy access to Kilo Code and your file browser at the same time. 

>Just right click on the Kilo Code icon and say "Move to" --> "Secondary side bar"