# Skills

This directory contains skills that extend agent capabilities with specialized knowledge and workflows.

For a complete list of available components, see [opencode/README.md](../README.md#available-components).

## About Skills

Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. Each skill is a folder containing a `SKILL.md` file with metadata and instructions that tell an agent how to perform a specific task.

## Structure
Each skill follows this structure:
- `skill-name/` - Directory named after the skill
  - `SKILL.md` - Contains the skill definition with YAML frontmatter and Markdown instructions

## Available Skills

| Skill Name | Description | Output |
|------------|-------------|--------|
| `example-skill` | An example skill to demonstrate the skill format and capabilities. Activate when asked to create new skills, learn about skill structure, demonstrate skill format, show skill examples, or when you need a template for creating new skills. | Template/reference only |
| `internet-search-searxng` | Search the internet using SearXNG metasearch engine and use results for planning or coding tasks. Activate when asked to search online, find current information, research topics, check the internet for data, browse web, look up information, or when you need current data for coding tasks. | Search results (returned directly) |
| `new-assignment` | Workflow to plan and prepare for implementing a new assignment when a user asks to start work on an issue, ticket, or assignment. | Plan files in `~/.agents/plans/` |
| `research` | Workflow to gather context and explore relevant information when a user asks to investigate a topic, ticket, or code area before planning or coding. | Context files in `~/.agents/context/` |

## Creating Skills

Skills use YAML frontmatter followed by Markdown content containing the instructions:

```yaml
---
name: my-skill-name
description: A brief description of what this skill does and when to use it
---
# Instructions

Your detailed instructions for the AI agent go here.
```

## Usage

### Automatic Activation
Skills are automatically loaded by OpenCode when the workspace initializes. The agent will recognize when a skill's description matches the user's request and load the full instructions into context.

### Manual Invocation (Slash Commands)
Skills can also be manually invoked using slash commands:
- `/research <topic>` - Trigger research skill
- `/new-assignment <ticket>` - Trigger new-assignment skill
- `/internet-search <query>` - Trigger internet-search skill
- `/example-skill` - Trigger example-skill

For more information about creating and using skills, visit: https://opencode.ai/docs/skills