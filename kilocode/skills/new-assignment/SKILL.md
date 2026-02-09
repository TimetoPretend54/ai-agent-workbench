---
name: new-assignment
description: Workflow to plan and prepare for implementing a new assignment when a user asks to start work on an issue, ticket, or assignment.
---

# New Assignment Setup

## When to Use
Use this skill when:
- User mentions a ticket/issue/assignment number (e.g., "PROJ-1234", "TICKET-123")
- User says "start working on issue X" / "start working on ticket X"
- User mentions "new ticket" / "new issue" or "implementing issue"
- User provides acceptance criteria for a new feature

## Example Usage
- "Start work on PROJ-1234"
- "Begin ticket TKT-789"
- "Plan XYZ module"
- "Start working on XYZ"

## Skill Reference

**Skill name:** `new-assignment`
**Relative path:** `kilocode/skills/new-assignment/SKILL.md`
**Home directory path:** `~/.kilocode/skills/new-assignment/SKILL.md`
(Expands to absolute path: Unix/Linux/macOS: `/home/user/.kilocode/...`, Windows: `C:\Users\user\.kilocode\...`)

## Overview
Structured workflow to plan and prepare for implementing a new assignment / issue / ticket, ensuring thorough understanding before coding begins.

### Input
Assignment Number (if applicable): {ASSIGNMENT_NUMBER}
Base Branch (if applicable): {BASE_BRANCH}
Title: {ISSUE_TITLE}
Acceptance Criteria: {AC_CRITERIA}
Additional Info (if applicable): {ADDITIONAL_INFO}

### Normalization Rules
- Assignment number: uppercase
- short_name: lowercase snake_case
- Derive short_name from ISSUE_TITLE: convert to lowercase, replace spaces and special characters with underscores, collapse multiple consecutive separators into a single underscore, trim leading/trailing underscores. Example: "Fix Login Bug" → "fix_login_bug". Example with consecutive separators: "Feature   XYZ" → "feature_xyz"

### Goal / Outcome
Produce a verified plan for an assignment that another code agent or user can follow to implement features safely and efficiently.

### System File References
**IMPORTANT**: Paths like `~/.kilocode/system/skills/engineering-principles.md` are **executable paths** pointing to where system files are located. These paths must be used in `execute_command` calls to access shared resources. They are absolute paths anchored at the user's home directory.

### File Storage Location
**IMPORTANT**: All files under `~/.kilocode/` (including plans, context, and system files) are stored in the **home directory**, NOT relative to the current working directory. This is an absolute path anchored at the user's home directory:
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
**Input Sanitization**: Before using ASSIGNMENT_NUMBER or ISSUE_TITLE in file paths or commands:
- Remove directory separators (`/`, `\`, `..`) to prevent path traversal.
- Replace spaces and special characters with underscores (the Normalization Rules already enforce snake_case, which meets this requirement).
- Allow only alphanumeric, hyphens, and underscores in final file names.
- Ensure proper quoting in shell commands to prevent injection attacks.

### Engineering Principles
This skill enforces the engineering principles defined in `~/.kilocode/system/skills/engineering-principles.md`. The skill's steps and quality checklist ensure each principle is addressed:

1. **DRY**: Step 6 (Reuse Existing Patterns) identifies reusable components, utilities, and design tokens to avoid duplication.
2. **Scalability**: Step 10 (Create Implementation Plan) organizes work into phases for larger assignments and evaluates performance implications and scaling strategies.
3. **Architectural Risk Analysis**: Steps 8 (Analyze Backend / Dependencies) and 9 (Trace Data Sources) analyze dependencies, compatibility constraints, and data flow to identify risks and mitigation strategies.
4. **Operational & Reliability**: Step 8 (Analyze Backend / Dependencies) documents failure modes, recovery procedures, and observability requirements; the quality checklist ensures these are covered.
5. **Security & Safety**: Steps 5 (Research External Best Practices), 8 (Analyze Backend / Dependencies), and 9 (Trace Data Sources) address data exposure risks, dependency trust assessment, and safe defaults; the quality checklist verifies these.
6. **Testability & Change Safety**: Step 10 (Create Implementation Plan) defines testing strategy and change isolation mechanisms; Step 11 (Verify AC Alignment) ensures test coverage; the quality checklist confirms testing seams and isolation.

Reference: `~/.kilocode/system/skills/engineering-principles.md`

## Steps

**Mode Management**: This skill involves planning and analysis work. Use the `switch_mode` tool to switch to **architect** mode at the start and remain in architect mode throughout all planning steps. Do NOT switch to code mode - this skill stops before implementation.

0. Confirm Base Branch & Design Availability
- Check if the user explicitly provided a base branch in their request.
- If YES: use it and skip confirmation.
- If NO: ask the user which base branch to use. Suggested question: "What base branch should I use for this assignment?"
- Provide recommendations: origin/dev (suggested), main, release/*
- Wait for confirmation before proceeding.
- Base Branch Rules:
  - Always suggest origin/dev first
  - Avoid defaulting to origin/main unless explicitly confirmed
  - Rationale: Choosing the appropriate base branch ensures the assignment integrates smoothly with existing work and minimizes merge conflicts. Prefer branches that reflect the target environment (dev for ongoing development, main for production, release/* for versioned releases).
- Also ask: "Are there any design mockups, Figma links, or UI specifications available?" to determine if design verification (Step 7) is needed
- **IMMEDIATELY sanitize {ASSIGNMENT_NUMBER} and {ISSUE_TITLE}** according to Security Considerations (Section above). Remove directory separators, replace spaces/special characters with underscores, allow only [a-zA-Z0-9_-]. Do this BEFORE any file operations or pattern construction.

1. Check for Existing Work
- Verify the `~/.kilocode/plans/` and `~/.kilocode/context/` directories exist using execute_command with the directory existence check pattern from `~/.kilocode/system/skills/cross-platform-commands.md`.
- If missing, create them using the directory creation pattern.
- Check Git branches using execute_command with platform-specific commands:
  - Unix/Linux/macOS: `git branch --list`
  - Windows PowerShell: `git branch --list` (git works in PowerShell) or use the pattern from `~/.kilocode/system/skills/cross-platform-commands.md`
- Search for existing plan and context files using the pattern searching commands from the cross-platform file.
- If existing work is found, check its modification timestamp using the file info pattern. If older than 30 days, note: "Existing work is stale (over 30 days old); updating is recommended."
- If existing work is found, ask: "I found existing work for this assignment. Should I review and update it, or start fresh?"

2. Check for Related Work
- Look for related plans and context files
- Check supporting docs

3. Maintain Context Files
- Add new context for undocumented patterns or architecture
- Update existing context files if outdated
- Perform this iteratively
- Reference: ~/.kilocode/system/skills/context.md

4. Explore the Codebase
- Identify repositories involved
- Read README, .kilocode rules, and local dev instructions
- Trace data flow and component relationships
- Understand mocking and test setup
- Document findings in context files
- For repositories within the workspace: use the search_files tool with:
  - path: the repository directory to search
  - regex: (?i){SANITIZED_ASSIGNMENT}
  - file_pattern: (optional) filter by file extension
  - **IMPORTANT**: Escape regex metacharacters in {ASSIGNMENT_NUMBER} before use. If the assignment contains `.`, `*`, `+`, `?`, `[`, `]`, `(`, `)`, `|`, `^`, `$`, or `\`, escape them (e.g., `.` becomes `\.`) to prevent regex syntax errors or injection.
  - file_pattern: (optional) filter by file extension
- For repositories outside the workspace: use execute_command with platform-specific search commands (e.g., grep, findstr, Select-String) as defined in ~/.kilocode/system/skills/cross-platform-commands.md to search those paths

5. Research External Best Practices (if applicable)
- Follow the standard pattern defined in: ~/.kilocode/system/skills/external-research.md
- This defines when to research, how to construct safe queries, security constraints, and documentation requirements
 - Invoke the internet-search-searxng skill following its defined workflow at: `~/.kilocode/skills/internet-search-searxng/SKILL.md`
- Ensure all search queries are sanitized (no project names, PII, or sensitive data)
- Document sources and verify alignment with planned implementation

6. Reuse Existing Patterns
- Search the codebase for similar components using search_files with appropriate regex patterns
- Check context files for documented patterns and design tokens
- Review existing style files, theme configurations, and constants
- Identify which patterns to follow and which to avoid
- Document specific files/utilities to reuse in the plan
- Ask if unsure which pattern is appropriate

7. Verify Designs (if provided)
- If design links or mockups are provided, review them thoroughly
- Note any discrepancies between designs and acceptance criteria
- Document verified design elements (colors, layout, interactions, typography)
- Capture diagrams or create ASCII diagrams if helpful
- Reference: Follow the detailed approach in research skill's Step 5

8. Analyze Backend / Dependencies
- Identify backend APIs, tickets, or external dependencies
- Document dependency status for each: ✅ Ready / ⏳ Pending / 🚧 Needs Mock
- Document mock strategies if needed
- Verify backward compatibility by following research skill's Step 8 (Document Existing Compatibility Constraints): check API versioning, deprecation policies, compatibility matrices
- Plan cleanup instructions for any temporary/mock code to be removed after implementation

9. Trace Data Sources
- Document origin of each data field (API, DB, config, JWT, etc.)
- Verify naming consistency

10. Create Implementation Plan
 - Verify the template exists at `~/.kilocode/skills/new-assignment/references/plan-template.md` using the file existence check pattern from `~/.kilocode/system/skills/cross-platform-commands.md`.
 - If template is missing, see Error Handling section below.
 - Read the template content from `~/.kilocode/skills/new-assignment/references/plan-template.md` using the file reading pattern from `~/.kilocode/system/skills/cross-platform-commands.md`.
 - Copy the plan template, replace placeholders ({ASSIGNMENT_NUMBER}, {Title}, etc.).
 - Save the plan to `~/.kilocode/plans/{ASSIGNMENT_NUMBER}_{SHORT_NAME}.plan.md` using execute_command with the file writing pattern from the cross-platform file.
- Fill in ALL sections of the template: Overview, Prerequisites, Data Sources, Mock Strategy, Implementation Phases, Files, Testing, AC Verification, Cleanup, Quick Start.
- In the Prerequisites section, use emoji status indicators with brief status notes as shown in the template.

11. Verify AC Alignment
- Walk through every AC item systematically
- Use the table format from the AC Verification Format section to document coverage
- Update the plan if any items are missing
- Ensure each AC item maps to a specific implementation phase or task

12. Update Iteratively
- As new information is discovered, update the plan immediately
- Don't wait - the plan should reflect current understanding
- Mark sections as "verified" vs "assumed" where appropriate

13. Ask Clarifying Questions & STOP
- Review all findings and identify gaps
- Ask user clarifying questions before finalizing
- STOP - do not proceed to implementation
- Present the plan and ask if anything is missing

14. STOP
- Do not implement code until user explicitly approves the plan
- Implementation is handled by a separate code execution phase

## Quality Checklist

Before presenting the plan, verify:
- [ ] Every AC item has a corresponding plan item
- [ ] Data sources are traced (where does each field come from?)
- [ ] Backend dependencies identified with mock strategy if needed
- [ ] Backward compatibility verified (safe to deploy incrementally?)
- [ ] **DRY principle applied**: Existing patterns/components reused; no unnecessary duplication
- [ ] **Scalability considered**: Phased implementation for larger work; performance implications addressed
- [ ] **Architectural risks identified**: Dependencies, coupling, breaking changes, and mitigation strategies documented
- [ ] **Operational & Reliability**: Failure modes, recovery procedures, observability requirements documented
- [ ] **Security & Safety**: Data exposure risks, dependency trust, safe defaults, and trust boundaries addressed
- [ ] **Testability & Change Safety**: Testing strategy defined, testing seams identified, change isolation planned
- [ ] File paths are explicit (NEW vs MODIFY)
- [ ] Cleanup instructions included for any temporary/mock code
- [ ] Implementation organized into phases (for larger assignments/work)
- [ ] Unit testing phase included with test examples
- [ ] Manual testing phase included with scenario checklist
- [ ] Quick Start section included with first file, key files, test commands
- [ ] A new agent/task could pick this up and start implementing immediately
- [ ] Context files updated with discoveries
- [ ] All referenced files verified to exist (templates, system files, plans directory)
- [ ] All commands are cross-platform compatible (no Unix-specific shell syntax)
- [ ] All file paths validated: execute_command commands use correct home directory expansion (`~` or `%USERPROFILE%`/`$HOME`)

## AC Verification Format

Use this table format when verifying AC alignment:

| AC Requirement | Plan Section / Phase | Status |
|----------------|---------------------|--------|
| {requirement} | {where in plan} | ✅/❌ |


## Error Handling

If `~/.kilocode/` directory doesn't exist:
- Create the directory structure using execute_command with appropriate platform-specific command (see cross-platform-commands.md for patterns)

If plan template is missing:
- Check if the template exists using execute_command with appropriate file existence check
- If missing, create a structured plan file with the standard sections (Overview, Prerequisites, Data Sources, Mock Strategy, Implementation Phases, Files, Testing, AC Verification, Cleanup, Quick Start) or notify the user

**Command Retry Guidance**: If an execute_command fails (non-zero exit code), retry up to 2 times with a brief pause using the cross-platform sleep patterns defined in ~/.kilocode/system/skills/cross-platform-commands.md before declaring failure. This handles transient issues like file locks or temporary network unavailability for mounted drives. If retries also fail, report the error and ask the user: "Command failed after retries. How would you like me to proceed? Retry again, skip this step, or abort?"

## References
 - Plan template: ~/.kilocode/skills/new-assignment/references/plan-template.md
 - Shared system patterns: ~/.kilocode/system/skills/*
 - Cross-platform commands: ~/.kilocode/system/skills/cross-platform-commands.md
