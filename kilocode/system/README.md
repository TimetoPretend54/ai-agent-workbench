# System Components

This directory contains system-level components and scripts that are available globally to Kilo Code workflows and skills.

## Structure
- `scripts/` - Contains utility scripts that can be accessed from any project context

## Global Access

You can create a symbolic link to make these system components available globally across all projects. This allows the scripts to be accessible from the global Kilo Code system directory.

### Windows
To create a symbolic link from this system directory to your global Kilo Code system directory:

```bash
# Link the system directory to the global system directory
mklink /D "%USERPROFILE%\.kilocode\system" "{path_to_repo}\kilocode\system"
```

Replace `{path_to_repo}` with the actual path to this repository on your system.

### Linux/Mac
```bash
# Create the symbolic link
ln -s {path_to_repo}/kilocode/system ~/.kilocode/system
```

**Note**: This provides a consistent path for accessing system scripts like `~/.kilocode/system/scripts/query_searxng.py` from any project context.

## Available Scripts
- `query_searxng.py` - Script for querying the SearXNG metasearch engine
- `start_searxng_agents.py` - Script for starting SearXNG services and agents