---
name: research
description: Workflow to gather context and explore relevant information when a user asks to investigate a topic, ticket, or code area before planning or coding.
---

# Research Setup

## When to Use
Use this skill when:
- User asks to gather context on an issue, topic, assignment, or ticket
- User wants to understand existing patterns, dependencies, or designs before planning work
- User wants information to prepare for coding, planning, or debugging

## Example Usage
- "Research PROJ-1234"
- "Gather context on ticket TKT-789"
- "Investigate XYZ module before implementing"
- "Find documentation and design references for feature ABC-12"
- "Check existing patterns for issue XYZ"

## Skill Reference

**Skill name:** `research`
**Relative path:** `kilocode/skills/research/SKILL.md`
**Home directory path:** `~/.kilocode/skills/research/SKILL.md`
(Expands to absolute path: Unix/Linux/macOS: `/home/user/.kilocode/...`, Windows: `C:\Users\user\.kilocode\...`)

## Overview
Structured workflow to gather, document, and create reusable knowledge and context relevant to assignments, features, or tickets.

### Input
Topic / Assignment Number (if applicable): {TOPIC_OR_ASSIGNMENT}
Specific questions or focus areas: {QUESTIONS}
Expected outcomes / deliverables (if applicable): {EXPECTED_OUTCOMES}
Additional Info (if applicable): {ADDITIONAL_INFO}

### Goal / Outcome
Produce a verified set of context files and notes that another code agent or user can immediately use to plan or implement features safely and efficiently.

### System File References
**IMPORTANT**: Paths like `~/.kilocode/system/skills/engineering-principles.md` are **executable paths** pointing to where system files are located. These paths must be used in `execute_command` calls to access shared resources. They are absolute paths anchored at the user's home directory.

### File Storage Location
**IMPORTANT**: All files under `~/.kilocode/` (including context files and system files) are stored in the **home directory**, NOT relative to the current working directory. This is an absolute path anchored at the user's home directory:
- Unix/Linux/macOS: `~/.kilocode/` (tilde expands to home directory)
- Windows: `%USERPROFILE%\.kilocode\` or `%HOME%\.kilocode\`

All references to `~/.kilocode/` throughout this skill (including system files like `~/.kilocode/system/skills/*`) refer to the home directory path appropriate for the operating system.

### Path Handling
**Tool Selection for Home Directory Paths**: All file operations targeting `~/.kilocode/` must use the `execute_command` tool with shell commands, NOT the `list_files`, `read_file`, or `search_files` tools. Those tools only accept workspace-relative paths and cannot expand tilde (`~`) to the home directory.

**Cross-Platform Command Patterns**: For each file operation, provide platform-specific command variants:
- **Unix/Linux/macOS**: Use standard shell commands (`ls`, `cat`, `grep`, `mkdir -p`, `test -f`, etc.)
- **Windows PowerShell**: Use PowerShell cmdlets (`Get-ChildItem`, `Get-Content`, `Select-String`, `Test-Path`, `New-Item`, etc.) with `$HOME` variable

**Example Pattern**:
```
- Unix/Linux/macOS: `command ~/.kilocode/path`
- Windows (PowerShell): `command "$HOME\.kilocode/path"`
```

**Note**: The `~` tilde expansion is a shell feature; when using `execute_command`, the command is passed to the system shell which performs the expansion automatically on Unix-like systems. On Windows, use explicit environment variables (`%USERPROFILE%` or `$HOME`) instead.

### Security Considerations
**Input Sanitization**: Before using TOPIC_OR_ASSIGNMENT in file paths or commands:
- Remove directory separators (`/`, `\`, `..`) to prevent path traversal.
- Replace spaces and special characters with underscores.
- Allow only alphanumeric, hyphens, and underscores in final file names.
- Ensure proper quoting in shell commands to prevent injection attacks.

### Engineering Principles
This skill enforces the engineering principles defined in `~/.kilocode/system/skills/engineering-principles.md`. The skill's steps and quality checklist ensure each principle is addressed:

1. **DRY**: Step 9 (Document Existing Patterns) identifies reusable components, utilities, and design tokens to avoid duplication.
2. **Scalability**: Step 10 (Document Architecture) evaluates system organization and growth considerations, including performance characteristics and scaling strategies.
3. **Architectural Risk Analysis**: Steps 7, 8, and 10 analyze dependencies, compatibility constraints, and architecture to identify risks and mitigation strategies.
4. **Operational & Reliability**: Step 7 (Identify Dependencies & Status) and the quality checklist require documenting failure modes, recovery procedures, and observability requirements.
5. **Security & Safety**: The quality checklist ensures data exposure risks, dependency trust assessment, and safe defaults are addressed.
6. **Testability & Change Safety**: Step 12 (Document Entry Points & Setup) and the quality checklist define testing strategy and change isolation mechanisms.

Reference: `~/.kilocode/system/skills/engineering-principles.md`


## Steps

**Mode Management**: This skill involves research and analysis work. Use the `switch_mode` tool to switch to **architect** mode at the start and remain in architect mode throughout all research steps. This is a planning/research skill only - do NOT switch to code mode.

0. Confirm Scope & Topic
- Clarify the research topic boundaries with the user
- Identify specific questions or focus areas
- Determine which repositories, documentation, and systems are involved
- If topic is unclear, ask: "What specific aspects of {TOPIC_OR_ASSIGNMENT} do you need to understand?"
- **IMMEDIATELY sanitize {TOPIC_OR_ASSIGNMENT}** according to Security Considerations (Section above). Remove directory separators, replace spaces/special characters with underscores, allow only [a-zA-Z0-9_-]. Do this BEFORE any file operations or pattern construction.
- Create a research question tracking table in the context file:
   | Question | Status | Source/Note |
   |----------|--------|-------------|
   | {question 1} | ☐ Pending / ☑ Answered | |
   | {question 2} | ☐ Pending / ☑ Answered | |


1. Check for Existing Research
- Verify the `~/.kilocode/context/` directory exists using execute_command with the directory existence check pattern from `~/.kilocode/system/skills/cross-platform-commands.md`.
- If missing, create it using the directory creation pattern.
- Search for existing context files matching the pattern `*{TOPIC_OR_ASSIGNMENT}*.md` using the pattern searching commands. Example:
  - Unix/Linux/macOS: `ls ~/.kilocode/context/*{SANITIZED_TOPIC}*.md 2>/dev/null`
  - Windows PowerShell: `Get-ChildItem "$HOME\.kilocode\context" -Filter "*{SANITIZED_TOPIC}*.md" -ErrorAction SilentlyContinue | Select-Object Name`
  - **IMPORTANT**: Sanitize {TOPIC_OR_ASSIGNMENT} first to remove glob metacharacters (`*`, `?`, `[`, `]`) to prevent pattern injection or unintended matches. Use only alphanumeric, hyphens, and underscores.
- If existing research is found, check its modification timestamp using file info commands (e.g., `ls -l` on Unix, `Get-Item` on PowerShell). If older than 30 days, note: "Existing research is stale (over 30 days old); updating is recommended."
- If existing research is found, ask: "I found existing context for this topic. Should I review and update it, or start fresh?"

2. Check for Related Work
- Identify which repositories are involved in this topic from the user's request and your understanding
- Look for related context files that may inform this research
- Check supporting docs, related tickets, or assignments
- Review any referenced materials from the user's request

3. Explore the Codebase
- For each repository involved:
  - Search for patterns in code, components, or modules
  - Trace data flows relevant to the topic
  - Understand the architecture and structure
  - For repositories within the workspace: use the search_files tool with:
    - path: the repository directory to search
    - regex: (?i){SANITIZED_TOPIC}
    - file_pattern: (optional) filter by file extension, e.g., "*.ts"
    - **IMPORTANT**: Escape regex metacharacters in {TOPIC_OR_ASSIGNMENT} before use. If the topic contains `.`, `*`, `+`, `?`, `[`, `]`, `(`, `)`, `|`, `^`, `$`, or `\`, escape them (e.g., `.` becomes `\.`) to prevent regex syntax errors or injection.
  - For repositories outside the workspace: use execute_command with platform-specific search commands (e.g., grep, findstr, Select-String) as defined in ~/.kilocode/system/skills/cross-platform-commands.md to search those absolute/relative paths
- Document file locations, key classes/functions, and search patterns

4. Research External Best Practices (if applicable)
- Applicability: Perform external research when working with frameworks, libraries, or technologies where current best practices matter (see: ~/.kilocode/system/skills/external-research.md for full criteria)
- Follow the standard pattern defined in: ~/.kilocode/system/skills/external-research.md
- This defines when to research, how to construct safe queries, security constraints, and documentation requirements
 - The internet-search-searxng skill is located at: `~/.kilocode/skills/internet-search-searxng/SKILL.md`
- Ensure all search queries are sanitized (no project names, PII, or sensitive data)
- Document sources and verify alignment with internal patterns

5. Verify Designs/Diagrams (if applicable)
- If design links or mockups are provided, review them thoroughly
- Note any discrepancies between designs and implementation
- Document verified design elements (colors, layout, interactions)
- Capture diagrams or create ASCII diagrams if helpful

6. Trace Data Sources Explicitly
- For each data field or flow relevant to the topic:
  - Document WHERE it comes from (API, DB, config, JWT, URL params, etc.)
  - Verify field names match between layers
  - Note any naming mismatches that need resolution
- Create a data sources table in the context file

7. Identify Dependencies & Status
- Identify related features, backend services, APIs, or data sources
- Document dependency status: ✅ Ready / ⏳ Pending / 🚧 Needs Mock
- For pending dependencies, note what's needed and when it will be available
- Include mock strategies if applicable

8. Document Existing Compatibility Constraints
- Research current API contracts, field names, and version requirements
- Identify any documented backward compatibility policies or versioning schemes
- Check for existing deprecation warnings or compatibility matrices
- Document current constraints: What changes would break existing clients based on the codebase as it exists today?
- Note any feature flags, environment variables, or configuration that control compatibility behavior

9. Document Existing Patterns
- Search for similar patterns already in the codebase
- Identify reusable components, utilities, or design tokens
- Note which patterns to follow and which to avoid
- Ask if unsure which pattern is appropriate

10. Document Architecture
- Describe how the system/module is organized
- Map key components and their relationships
- Include file structure and important directories
- Create diagrams if helpful (ASCII art or descriptions)

11. Create Context File
- Verify the template exists at `~/.kilocode/skills/research/references/context-template.md` using the file existence check pattern from `~/.kilocode/system/skills/cross-platform-commands.md`.
- If template is missing, see Error Handling section above.
- Read the template content from `~/.kilocode/skills/research/references/context-template.md` using the file reading pattern from `~/.kilocode/system/skills/cross-platform-commands.md`.
- Copy the context template and replace placeholders, fill in ALL sections.
- Save the context file to `~/.kilocode/context/{TOPIC_OR_ASSIGNMENT}.context.md` using execute_command with the file writing pattern from `~/.kilocode/system/skills/cross-platform-commands.md`.
- Ensure all template sections are completed: Overview, Research Questions, Key Findings (Architecture, Data Flow, Dependencies, Patterns), Code References, Constraints, Decisions, Verified Behaviors, Gaps & Assumptions, Testing & Mocking, Quick Reference, and References.

12. Document Entry Points & Setup
- Repositories involved with their purposes and locations
- Key configuration files and environment variables
- Local development commands (setup, start, build, test)
- Testing commands and mock data locations
- Initial exploration paths: which files to read first to understand the feature/module
- This enables future agents to quickly begin planning or implementation

13. Update Context Iteratively
- As new information is discovered, update the context file immediately
- Don't wait until the end - context should reflect current understanding
- Mark sections as "verified" vs "assumed" where appropriate
- Reference: ~/.kilocode/system/skills/context.md

14. Ask Clarifying Questions & STOP
- Review all findings and identify gaps
- Ask user clarifying questions before finalizing
- STOP - do not proceed to implementation (that's for new-assignment skill)
- Present the context file and ask if anything is missing

## Quality Checklist

Before completing research, verify:
- [ ] All key questions/areas have been addressed
- [ ] Sources documented with URLs or file paths
- [ ] Dependencies mapped with status (ready/mock/pending)
- [ ] Gaps and assumptions explicitly identified
- [ ] Context file created or updated
- [ ] Findings synthesized (not just raw data dump)
- [ ] **DRY principle addressed**: Reusable patterns, components, and utilities documented to prevent future duplication
- [ ] **Scalability evaluated**: Performance characteristics, capacity limits, and scaling strategies documented where applicable
- [ ] **Architectural risks identified**: Compatibility constraints, coupling issues, version conflicts, and mitigation strategies explicitly called out
- [ ] **Operational & Reliability**: Failure modes, recovery procedures, observability requirements, and health checks documented
- [ ] **Security & Safety**: Data exposure risks, dependency trust assessment, input sanitization, safe defaults, and trust boundaries addressed
- [ ] **Testability & Change Safety**: Testing strategy defined, testing seams identified, and change isolation mechanisms planned
- [ ] Quick reference pointers included for future planning
- [ ] A new agent/task could use this context to plan immediately
- [ ] Context file structure follows the template
- [ ] All referenced files verified to exist (templates, system files, context directory)
- [ ] All commands are cross-platform compatible (no Unix-specific shell syntax)
- [ ] All file paths validated: execute_command commands use correct home directory expansion (`~` or `%USERPROFILE%`/`$HOME`)

## Error Handling

If `~/.kilocode/` directory doesn't exist:
- Create the directory structure using execute_command with appropriate platform-specific command (see cross-platform-commands.md for patterns)

If context template is missing:
- Check if the template exists using execute_command with appropriate file existence check
- If missing, create a structured context file with all standard sections: Overview, Research Questions, Key Findings (Architecture, Data Flow, Dependencies, Patterns), Code References, Constraints, Decisions, Verified Behaviors, Gaps & Assumptions, Testing & Mocking, Quick Reference, and References
- Notify user if template cannot be found

**Command Retry Guidance**: If an execute_command fails (non-zero exit code), retry up to 2 times with a brief pause using the cross-platform sleep patterns defined in ~/.kilocode/system/skills/cross-platform-commands.md before declaring failure. This handles transient issues like file locks or temporary network unavailability for mounted drives. If retries also fail, report the error and ask the user: "Command failed after retries. How would you like me to proceed? Retry again, skip this step, or abort?"

## References
 - Shared system patterns: ~/.kilocode/system/skills/*
 - Context files: ~/.kilocode/context/*.md
 - Context template: ~/.kilocode/skills/research/references/context-template.md
 - Cross-platform commands: ~/.kilocode/system/skills/cross-platform-commands.md
