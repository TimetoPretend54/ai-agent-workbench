# Workflows

This directory contains workflow definitions that automate repetitive tasks by defining step-by-step instructions for Kilo Code to execute.

For a complete list of available components (including both skills and workflows), see [kilocode/README.md#available-components](../README.md#available-components).

## Usage
Invoke any workflow by typing `/[workflow-name.md]` in the chat.

## Creating Workflows
Workflows are markdown files that contain step-by-step instructions. Each workflow file should contain:
1. A clear title and description
2. Step-by-step instructions for the task
3. Any required parameters or inputs
4. References to tools that should be used (e.g., `search_files()`, `execute_command()`, `read_file()`)

## Example Workflow Structure
```markdown
# Workflow Title

Description of what this workflow does.

Steps:
1. First step using `search_files()` to locate specific content
2. Second step using `execute_command()` to run a CLI command
3. Third step using `read_file()` to examine specific files
4. Final step with any required follow-up actions
```

For more information about creating workflows, visit: https://kilo.ai/docs/customize/workflows