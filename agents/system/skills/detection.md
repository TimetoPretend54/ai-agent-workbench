# Existing Work Detection Rules

Before creating new plans or context files:

1. Check if a relevant file already exists
2. If found, warn the user
3. Offer a choice:
   a) Reuse and continue
   b) Start fresh (overwrite or extend)

Never silently overwrite existing files.

Detection applies to:
- Plan files
- Context files
- Git branches (if applicable)
