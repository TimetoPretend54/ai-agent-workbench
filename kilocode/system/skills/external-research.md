# External Best Practices Research

This document defines the standard pattern for researching external best practices, documentation, and current information using the `internet-search-searxng` skill.

---

## Purpose

When working with frameworks, libraries, or technologies where current documentation matters, agents should verify internal patterns against up-to-date external sources.

---

## When to Use

Invoke external research when:
- Implementing features using frameworks/libraries (React, Django, Spring, etc.)
- Checking security advisories or deprecation notices
- Verifying version compatibility requirements
- Exploring community solutions to common problems
- Validating that implementation approaches follow current best practices

---

## Skill Reference

**Skill name:** `internet-search-searxng`  
**Relative path:** `kilocode/skills/internet-search-searxng/SKILL.md`

---

## Search Query Construction

### CRITICAL Security Constraint

**NEVER** include sensitive information in search queries. Construct queries using only generic technology/language terms.

**Forbidden content:**
- Project names, ticket numbers, or company identifiers
- Specific bug details or internal system information
- URLs, endpoints, or internal addresses
- Any PII or sensitive data
- Internal code snippets or proprietary information

### Safe Query Examples

✅ **Safe:**
- "React best practices 2024"
- "OAuth2 implementation guide"
- "Python async await patterns"
- "Docker security best practices"
- "PostgreSQL connection pooling configuration"

❌ **Unsafe:**
- "PROJ-1234 authentication bug fix" (contains project ID)
- "how to fix error in https://internal.company.com/api" (contains internal URL)
- "John Smith password reset implementation" (contains PII)
- "our proprietary caching algorithm optimization" (contains proprietary info)

---

## Implementation Pattern

1. **Identify need:** Determine if the task involves technology where current best practices matter
2. **Construct query:** Use only generic terms (technology name + topic + year if relevant)
3. **Invoke skill:** Call `internet-search-searxng` with the sanitized query
4. **Document sources:** Record URLs and dates accessed for traceability
5. **Compare:** Verify internal patterns align with external recommendations
6. **Note discrepancies:** Document any gaps between internal implementation and current best practices
7. **Proceed accordingly:** Follow best practices or document why deviation is necessary

---

## Documentation Requirements

When external research is performed, include in your output:
- Search queries used (sanitized version)
- Sources consulted (URLs + access dates)
- Key findings relevant to the task
- Any discrepancies identified
- Decision rationale if deviating from best practices

---

## Relative Path for Skill Invocation

When referencing this skill from other skills or workflows, use the relative path:
`kilocode/skills/internet-search-searxng/SKILL.md`

This ensures agents can locate the skill definition regardless of workspace location.

---

## Examples by Context

**Frontend development:** "React hooks best practices 2024", "TypeScript strict mode guide"  
**Backend APIs:** "REST API authentication patterns", "GraphQL vs REST 2024"  
**Security:** "OWASP Top 10 2024", "JWT token expiration best practices"  
**DevOps:** "Kubernetes security hardening", "CI/CD pipeline best practices"  
**Databases:** "PostgreSQL indexing strategies", "MongoDB connection pooling"

---

## Notes

- External research is **optional** but recommended for technologies with frequent updates
- If research reveals critical security issues, treat as high priority
- When in doubt about query safety, err on the side of more generic terms
- Always validate that sources are authoritative (official docs, reputable security sites, well-known community resources)
