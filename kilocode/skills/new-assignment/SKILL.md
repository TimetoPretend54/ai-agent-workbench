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
- "Implement XYZ module"
- "Start working on XYZ"

## Overview
Structured workflow to plan and prepare for implementing a new assignment / issue / ticket, ensuring thorough understanding before coding begins.

### Goal / Outcome
Quickly produce a verified plan for an assignment that another code agent or user can follow to implement features safely and efficiently.

## Input
Assignment Number (if applicable): {ASSIGNMENT_NUMBER}
Title: {ISSUE_TITLE}

Normalization:
- Assignment number: uppercase
- short_name: lowercase snake_case

## Steps

**Mode Management**: This skill involves planning and analysis work. Use the `switch_mode` tool to switch to **architect** mode at the start and remain in architect mode throughout all planning steps. Do NOT switch to code mode - this skill stops before implementation.

0. Confirm Base Branch
- Check if the user explicitly provided a base branch in their request.
- If YES: use it and skip confirmation.
- If NO: ask the user which base branch to use.
What base branch should I use for this assignment?
Recommended: origin/dev
Other options: main, release/*
- Wait for confirmation before proceeding.
- Base Branch Rules:
  - Always suggest origin/dev first
  - Avoid defaulting to origin/main unless explicitly confirmed

1. Check for Existing Work
- Check Git branches, plans (~/.kilocode/plans/), context (~/.kilocode/context/)
git branch -a | grep -i {ASSIGNMENT_NUMBER}
ls ~/.kilocode/plans/ 2>/dev/null | grep -i {ASSIGNMENT_NUMBER}
ls ~/.kilocode/context/ 2>/dev/null | grep -i {ASSIGNMENT_NUMBER}
- If existing work is found, ask whether to reuse or start fresh

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
- Use cross-platform commands from ~/.kilocode/system/skills/cross-platform-commands.md

5. Research External Best Practices (if applicable)
- Follow the standard pattern defined in: ~/.kilocode/system/skills/external-research.md
- This defines when to research, how to construct safe queries, security constraints, and documentation requirements
- The internet-search-searxng skill is located at: kilocode/skills/internet-search-searxng/SKILL.md
- Ensure all search queries are sanitized (no project names, PII, or sensitive data)
- Document sources and verify alignment with planned implementation

6. Reuse Existing Patterns
- Search for similar patterns
- Use existing design tokens/styles
- Ask if unsure which pattern to follow

7. Verify Designs (if provided)
- Check design links or mockups
- Document verified elements
- Note discrepancies vs acceptance criteria

8. Analyze Backend / Dependencies
- Identify backend APIs, tickets, or external dependencies
- Document mock strategies if needed
- Verify backward compatibility

9. Trace Data Sources
- Document origin of each data field (API, DB, config, JWT, etc.)
- Verify naming consistency

10. Create Implementation Plan
- Copy the plan template from ~/.kilocode/skills/new-assignment/references/plan-template.md
- Replace placeholders ({ASSIGNMENT_NUMBER}, {Title}, etc.)
- Save to ~/.kilocode/plans/{ASSIGNMENT_NUMBER}_{short_name}.plan.md
- Include all phases, dependencies, mock strategy, testing, AC verification, quick start, and cleanup

10. Verify AC Alignment
- Walk through every AC item
- Update the plan if any items are missing

11. Update Iteratively
- Add discoveries immediately
- Mark sections as verified vs assumed

12. Ask Clarifying Questions
- Stop and clarify before implementation

13. STOP
- Do not implement code until user approves plan

## Quality Checklist

Before presenting the plan, verify:
- [ ] Every AC item has a corresponding plan item
- [ ] Data sources are traced (where does each field come from?)
- [ ] Backend dependencies identified with mock strategy if needed
- [ ] Backward compatibility verified (safe to deploy incrementally?)
- [ ] Existing patterns searched before proposing new ones
- [ ] File paths are explicit (NEW vs MODIFY)
- [ ] Cleanup instructions included for any temporary/mock code
- [ ] Implementation organized into phases (for larger assignments/work)
- [ ] Unit testing phase included with test examples
- [ ] Manual testing phase included with scenario checklist
- [ ] Quick Start section included with first file, key files, test commands
- [ ] A new agent/task could pick this up and start implementing immediately
- [ ] Context files updated with discoveries

## AC Verification Format

Use this table format when verifying AC alignment:

| AC Requirement | Plan Coverage | Status |
|----------------|---------------|--------|
| {requirement} | {where in plan} | ✅/❌ |

## Error Handling

If `~/.kilocode/` directory doesn't exist:
```bash
mkdir -p ~/.kilocode/{plans,context}
```

If plan template is missing:
- Check: `ls ~/.kilocode/skills/new-assignment/references/plan-template.md`
- If missing, create from the skill's reference section or notify user

## References
- Plan template: ~/.kilocode/skills/new-assignment/references/plan-template.md
- Shared system patterns: ~/.kilocode/system/skills/*
- Cross-platform commands: ~/.kilocode/system/skills/cross-platform-commands.md
