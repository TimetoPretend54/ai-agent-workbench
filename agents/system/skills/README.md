# Shared Skill System

This directory contains shared logic and conventions used by multiple skills (Kilo Code, OpenCode, etc.).

These files define:
- Filesystem layout
- Cross-platform command patterns
- Detection and reuse rules
- Context maintenance standards

Skills in ~/.agents/system/skills may reference these files but should not duplicate their contents.

Do not place task-specific instructions here.
