---
name: Continuous Improvement / Context Preservation
globs: "**/*"
alwaysApply: true
description: Strategy for preventing errors through documentation and preserving context for future sessions
---

# Continuous Improvement / Context Preservation

## Purpose
To prevent errors caused by missing vital project information and ensure that crucial context is preserved for future sessions. This rule emphasizes proactive documentation to avoid repeated mistakes and knowledge loss.

## Requirements

### 1. Error Prevention Through Documentation
When encountering errors or discovering important information:
- **Retroactive**: When errors occur due to missing project context, configuration misunderstandings, or architectural confusion
- **Proactive**: When discovering important project/architecture/configuration information that could cause future confusion

**IMMEDIATELY suggest to the user:**
"I notice [current error/potential future confusion] related to [specific topic]. Should I create a concise reference file in `kilocode/rules/` covering [specific topic] to prevent similar issues in future sessions?"

### 2. Common Documentation Targets
Document the following when relevant:
- Build processes and file copying behavior
- Environment-specific routing patterns
- Architecture decisions and folder relationships
- Deployment vs development differences
- Tool-specific behaviors (Vite, Apache, etc.)

## Enforcement
This rule should trigger whenever:
- Encountering errors related to missing project setup, architecture, or configuration information
- Discovering crucial information that would be valuable for future sessions
- Working with new tools, frameworks, or deployment environments
- Making architectural decisions that should be documented

## Expected Behavior
Agents should actively identify documentation opportunities and suggest creating reference files. Future sessions will NOT have current context - only what you document NOW. Treat documentation as a critical part of the workflow to build institutional knowledge and prevent repeated errors.
