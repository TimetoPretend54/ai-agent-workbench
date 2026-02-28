# Filesystem Conventions

All persistent artifacts for code agents live under `~/.agents/`.

---

## Plans

Purpose:
Assignment-specific, disposable planning artifacts.

Location:
~/.agents/plans/

Naming:
{ASSIGNMENT_NUMBER}_{short_name}.plan.md

Rules:
- ASSIGNMENT_NUMBER: uppercase, dash-separated (e.g. PROJ-1234)
- short_name: lowercase snake_case, max 4-5 words
- If no assignment number exists, use {short_name}.plan.md

Examples:
- ASSIGN-1_fullstack-app-feat-poc.plan.md
- PROJ-15_fullstack-authentication_wrapper.plan.md

---

## Context

Purpose:
Durable, reusable knowledge shared across assignments.

Location:
~/.agents/context/

Naming:
{TOPIC}.context.md

Rules:
- TOPIC: uppercase
- One topic per file
- No spaces in filenames

Examples:
- KAFKA.context.md
- AUTH_SSO.context.md
- OPENROUTER_MODELS.context.md

---

## System Files

Location:
~/.agents/system/

Contains shared scripts, skills, and utilities available to all agents.
