# Continuous Improvement / Context Preservation Strategy

## Error Prevention Through Documentation

When
- encountering errors that occurred due to lack of vital information like project setup, architecture, configuration or similar
OR
- discovering crucial information whose inavailability could cause such errors in the future:

**IMMEDIATELY suggest to the user:**
"I notice [current error/potential future confusion] related to [specific topic]. Should I create a concise reference file in `.kilocode/rules/` covering [specific topic] to prevent similar issues in future sessions?"

**Trigger conditions:**
- **Retroactive**: Current errors from missing project context, configuration misunderstandings, or architectural confusion
- **Proactive**: Discovery of important project/architecture/configuration information that could cause future session confusion

## Common Documentation Targets
- Build processes and file copying behavior
- Environment-specific routing patterns
- Architecture decisions and folder relationships
- Deployment vs development differences
- Tool-specific behaviors (Vite, Apache, etc.)

**Key principle:** Future sessions will NOT have current context - only what you document NOW.
