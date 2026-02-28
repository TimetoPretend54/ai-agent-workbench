# Commands

This directory contains custom commands for OpenCode that can be executed with `/command-name`.

## Available Commands

| Command | Description |
|---------|-------------|
| /research | Research a topic, ticket, or code area |
| /new-assignment | Start work on a new assignment or ticket |
| /internet-search | Search the internet using SearXNG |
| /example-skill | Learn about skill format and creation |
| /skill-call-template | Template for triggering any skill |

## Usage

Type `/` followed by the command name in the OpenCode TUI:

```
/research PROJ-1234
/new-assignment TICKET-567
/internet-search OpenCode documentation
/example-skill
```

## Creating Commands

Commands are markdown files with YAML frontmatter:

```yaml
---
description: Your command description
agent: architect  (optional)
---
Your prompt here: $ARGUMENTS
```

For more information, visit: https://opencode.ai/docs/commands
