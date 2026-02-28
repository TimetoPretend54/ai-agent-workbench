# System Components

This directory contains system-level components and scripts that are shared across code agents (Kilo Code, OpenCode, etc.).

## Structure
- `scripts/` - Contains utility scripts that can be accessed from any project context

## Global Access

You can create a symbolic link to make these system components available globally across all projects.

### Windows
```cmd
mklink /D "%USERPROFILE%\.agents" "{path_to_repo}\agents"
```

### Linux/Mac
```bash
ln -s {path_to_repo}/agents ~/.agents
```

**Note**: This provides a consistent path for accessing system scripts like `~/.agents/system/scripts/query_searxng.py` from any project context.

## Available Scripts
- `query_searxng.py` - Script for querying the SearXNG metasearch engine
- `start_searxng_agents.py` - Script for starting SearXNG services and agents
