# kilocode Directory

This directory contains project-specific configurations and workflows for Kilo Code integration.

## Why not .kilocode? Global KiloCode Repo
Sets a Global symlink, to avoid duplicating rules into context, avoid using `.kilocode`

## Available Components

| Component Name | Type | Description | Can Trigger as Workflow |
|----------------|------|-------------|------------------------|
| | internet-search-searxng | Skill | Search the internet using SearXNG metasearch engine and use results for planning or coding tasks | Yes |
| | example-skill | Skill | An example skill to demonstrate the skill format and capabilities | Yes |
| | research | Skill | Workflow to gather context and explore relevant information when a user asks to investigate a topic, ticket, or code area before planning or coding. | Yes |
| | new-assignment | Skill | Workflow to plan and prepare for implementing a new assignment when a user asks to start work on an issue, ticket, or assignment. | Yes |

## Global System Setup

To use the global system components (scripts, docker configs) across multiple workspaces, create a symlink:

This allows global access to system scripts like `~/.kilocode/system/scripts/query_searxng.py` from any project context.

Replace `{path_to_repo}` with the actual path to this repository on your system.

### Mac/Linix
```bash
# From your home directory, create a symlink to the system kilocode directory
ln -s {path_to_repo}/kilocode/ ~/.kilocode/
```

### Windows
Or on Windows (Command Prompt as Administrator):
```bash
mklink /D %USERPROFILE%\.kilocode {path_to_repo}\kilocode
```
- Powershell: prefix w/ `cmd /c`

## Structure
- `workflows/` - Contains workflow definitions that automate repetitive tasks by defining step-by-step instructions for Kilo Code to execute
  - NOTE: Skills should be used instead if possible
  - Use `workflows/` to trigger the skill manually
- `skills/` - Contains skills that extend agent capabilities with specialized knowledge and workflows  
- `system/` - Contains system components including scripts and docker configurations

## Purpose
The `kilocode` directory follows the Kilo Code standard structure for project customization, enabling automated workflows and custom configurations specific to this project.

For more information about Kilo Code workflows, visit: https://kilo.ai/docs/customize/workflows

## Ongoing Issues
- [] https://github.com/Kilo-Org/kilocode/issues/5256
  - Had to revert to 4.145.0, introduced in v4.146.0
  - Current version still broken: 5.4.0
  - Waiting for Fix: https://github.com/Kilo-Org/kilocode/pull/5377
- [] https://github.com/Kilo-Org/kilocode/discussions/5443
  - Waiting for manually triggering skills
- [X] https://github.com/Kilo-Org/kilocode/issues/4498
  - OpenRouter Provider forces token cost for Autocomplete
  - Need support to manually select
  - Otherwise getting charged even when selecting free model
  - EDIT: FIXED, Can now turn off autocomplete via settings again
- [] https://github.com/Kilo-Org/kilocode/discussions/1563
  - Preview Diff/Changes (similar to Cursor)
