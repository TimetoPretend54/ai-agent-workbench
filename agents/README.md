# agents Directory

This directory contains shared components for multiple code agents (Kilo Code, OpenCode, etc.).

## Structure

- `kilocode/` - KiloCode-specific files (workflows, rules)
- `opencode/` - OpenCode-specific files (commands, AGENTS.md)
- `skills/` - Universal skills (shared by all agents)
- `context/` - Context files directory
- `plans/` - Plan files directory
- `system/` - Shared system files (scripts, docker configs)

## Why Unified Storage?

Agents use `~/.agents/` as the single location for all persistent resources:

| Resource | Location |
|----------|----------|
| Skills | `~/.agents/skills/` |
| Context | `~/.agents/context/` |
| Plans | `~/.agents/plans/` |
| System files | `~/.agents/system/` |

This follows the [OpenCode skills standard](https://opencode.ai/docs/skills/) where skills are discovered from config directories like `~/.config/opencode/skills/`, which are symlinked to the shared `agents/skills/`.

## Global Setup

### Windows
Run in **Command Prompt as Administrator**:
```cmd
:: Shared agents config (contains skills, context, plans, system)
mklink /D %USERPROFILE%\.agents {path_to_repo}\agents

:: KiloCode global config (workflows, rules)
mklink /D %USERPROFILE%\.kilocode {path_to_repo}\agents\kilocode

:: OpenCode global config (commands, AGENTS.md)
:: Note: Full directory symlink; may include OpenCode project files
mklink /D %USERPROFILE%\.config\opencode {path_to_repo}\agents\opencode
```

### Mac/Linux
```bash
ln -s {path_to_repo}/agents ~/.agents
ln -s {path_to_repo}/agents/kilocode ~/.kilocode
ln -s {path_to_repo}/agents/opencode ~/.config/opencode
```

## Access Paths

- **Shared system**: `~/.agents/system/`
- **Skills**: `~/.agents/skills/`
- **Context**: `~/.agents/context/`
- **Plans**: `~/.agents/plans/`
- **KiloCode**: `~/.kilocode/`
- **OpenCode**: `~/.config/opencode/`

Note: `~/.config/opencode/` cannot be fully symlinked because it contains other files (node_modules, package.json, bun.lock, .gitignore) - only specific subdirectories (commands, skills) are symlinked.
