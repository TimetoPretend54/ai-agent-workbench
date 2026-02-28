# Skills

This directory contains skills that extend agent capabilities with specialized knowledge and workflows.

For a complete list of available components, see [opencode/README.md](../README.md#available-components).

## About Skills

Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. Each skill is a folder containing a `SKILL.md` file with metadata and instructions that tell an agent how to perform a specific task.

## Structure
Each skill follows this structure:
- `skill-name/` - Directory named after the skill
  - `SKILL.md` - Contains the skill definition with YAML frontmatter and Markdown instructions

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

Skills are automatically loaded by OpenCode when the workspace initializes. The agent will recognize when a skill's description matches the user's request and load the full instructions into context.

For more information about creating and using skills, visit: https://opencode.ai/docs/skills