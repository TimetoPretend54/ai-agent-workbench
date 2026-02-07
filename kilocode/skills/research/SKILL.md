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

## Overview
Structured workflow to gather, document, and maintain reusable knowledge and context relevant to assignments, features, or tickets.

### Goal / Outcome
Produce a verified set of context files and notes that another code agent or user can immediately use to plan or implement features safely and efficiently.

## Input
Topic / Assignment Number (if applicable): {TOPIC_OR_ASSIGNMENT}
Specific questions or focus areas: {QUESTIONS}

## Steps

**Mode Management**: This skill involves research and analysis work. Use the `switch_mode` tool to switch to **architect** mode at the start and remain in architect mode throughout all research steps. This is a planning/research skill only - do NOT switch to code mode.

0. Confirm Scope & Topic
- Clarify the research topic boundaries with the user
- Identify specific questions or focus areas
- Determine which repositories, documentation, and systems are involved
- If topic is unclear, ask: "What specific aspects of {TOPIC} do you need to understand?"

1. Check for Existing Research
- Check if context already exists for this topic
ls ~/.kilocode/context/ | grep -i {TOPIC_OR_ASSIGNMENT}
- Read existing context files to avoid duplication
- If existing research is found, ask: "I found existing context for this topic. Should I review and update it, or start fresh?"

2. Check for Related Work
- Look for related context files that may inform this research
- Check supporting docs, related tickets, or assignments
- Review any referenced materials from the user's request

3. Explore the Codebase
- For each repository involved:
  - Search for patterns in code, components, or modules
  - Trace data flows relevant to the topic
  - Understand the architecture and structure
  - Use cross-platform commands from ~/.kilocode/system/skills/cross-platform-commands.md
grep -Ri "{TOPIC_OR_ASSIGNMENT}" path/to/repos
- Document file locations, key classes/functions, and search patterns

4. Research External Best Practices (if applicable)
- Follow the standard pattern defined in: ~/.kilocode/system/skills/external-research.md
- This defines when to research, how to construct safe queries, security constraints, and documentation requirements
- The internet-search-searxng skill is located at: kilocode/skills/internet-search-searxng/SKILL.md
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

6. Identify Dependencies & Status
- Identify related features, backend services, APIs, or data sources
- Document dependency status: ✅ Ready / ⏳ Pending / 🚧 Needs Mock
- For pending dependencies, note what's needed and when it will be available
- Include mock strategies if applicable

7. Document Existing Compatibility Constraints
- Research current API contracts, field names, and version requirements
- Identify any documented backward compatibility policies or versioning schemes
- Check for existing deprecation warnings or compatibility matrices
- Document current constraints: What changes would break existing clients based on the codebase as it exists today?
- Note any feature flags, environment variables, or configuration that control compatibility behavior

8. Document Existing Patterns
- Search for similar patterns already in the codebase
- Identify reusable components, utilities, or design tokens
- Note which patterns to follow and which to avoid
- Ask if unsure which pattern is appropriate

9. Document Architecture
- Describe how the system/module is organized
- Map key components and their relationships
- Include file structure and important directories
- Create diagrams if helpful (ASCII art or descriptions)

10. Create Context File
- Copy the context template from ~/.kilocode/skills/research/references/context-template.md
- Replace placeholders and fill in all sections
- Save to: ~/.kilocode/context/{TOPIC_OR_ASSIGNMENT}_CONTEXT.md
- Include: research questions, findings, architecture, data flow, dependencies, patterns, code references, constraints, decisions, gaps, quick reference

11. Document Entry Points & Setup
- Repositories involved with their purposes and locations
- Key configuration files and environment variables
- Local development commands (setup, start, build, test)
- Testing commands and mock data locations
- Initial exploration paths: which files to read first to understand the feature/module
- This enables future agents to quickly begin planning or implementation

12. Update Context Iteratively
- As new information is discovered, update the context file immediately
- Don't wait until the end - context should reflect current understanding
- Mark sections as "verified" vs "assumed" where appropriate
- Reference: ~/.kilocode/system/skills/context.md

13. Ask Clarifying Questions & STOP
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
- [ ] Quick reference pointers included for future planning
- [ ] A new agent/task could use this context to plan immediately
- [ ] Context file structure follows the template

## Error Handling

If `~/.kilocode/` directory doesn't exist:
```bash
mkdir -p ~/.kilocode/context
```

If context template is missing:
- Check: `ls ~/.kilocode/skills/research/references/context-template.md`
- If missing, create a structured context file with sections: Overview, Key Facts, Constraints, Decisions, Verified Behaviors, References
- Notify user if template cannot be found

## References
- Shared system patterns: ~/.kilocode/system/skills/*
- Context files: ~/.kilocode/context/*.md
- Context template: ~/.kilocode/skills/research/references/context-template.md
- Cross-platform commands: ~/.kilocode/system/skills/cross-platform-commands.md
