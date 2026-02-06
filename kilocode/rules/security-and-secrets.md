---
name: Security and Secrets Management
globs: "**/*"
alwaysApply: true
description: Guidelines for handling sensitive data, credentials, and security best practices
---

# Security and Secrets Management

## Purpose
Prevent security vulnerabilities by ensuring proper handling of credentials, sensitive data, and maintaining secure agent operations.

## Requirements

### 1. Never Hardcode Secrets
- **NEVER** store API keys, tokens, passwords, or credentials in code
- **NEVER** commit secrets to version control, even in private repos
- **NEVER** include secrets in comments, logs, or error messages
- Use environment variables, configuration files, or secrets managers instead

### 2. Environment Variable Usage
- Load secrets from environment variables using appropriate libraries (e.g., `dotenv` for Python/Node.js)
- Validate that required environment variables are present before execution
- Use `.env` files for local development only - **NEVER** commit `.env` to version control
- Ensure `.env` is in `.gitignore`
- For production, use proper secrets management (Vault, AWS Secrets Manager, Azure Key Vault, etc.)

### 3. Data Privacy and PII Protection
- Minimize collection and processing of personally identifiable information (PII)
- Anonymize or pseudonymize sensitive data when possible
- Do not expose PII in logs, error messages, or agent outputs
- Follow data minimization principles: collect only what is necessary
- Implement data retention policies and automatic cleanup

### 4. Memory and State Security
- Isolate memory between users/sessions to prevent data leakage
- Set memory expiration and size limits
- Audit memory contents for sensitive data before persistence
- Use cryptographic integrity checks for long-term memory storage
- Never store authentication tokens or credentials in persistent memory without encryption

### 5. Input Validation and Sanitization
- Validate and sanitize all user inputs before processing
- Guard against prompt injection attacks
- Treat all external data as untrusted
- Implement context-aware permission frameworks
- Use allowlists over denylists for validation

### 6. External Access Control
- Apply principle of least privilege: agents should have only the minimum access required
- Use role-based access control (RBAC) for agent permissions
- When agents access data on behalf of users, inherit that user's permissions
- Never allow agents to access internal business data from public-facing interfaces
- Implement data loss prevention (DLP) policies

### 7. Secure Communication
- Use HTTPS/TLS for all external communications
- Verify SSL certificates when making requests
- Avoid sending sensitive data in URL parameters
- Encrypt sensitive data at rest and in transit
- Use secure APIs with proper authentication

### 8. Output Safety
- Filter agent outputs for sensitive information before presenting to users
- Implement content safety checks for generated content
- Redact or mask credentials, tokens, or PII in responses
- Review agent decisions for potential data exposure risks

### 9. Dependency Security
- Keep dependencies up to date to avoid known vulnerabilities
- Regularly scan for security vulnerabilities in dependencies
- Use trusted, official APIs and connectors instead of custom integrations
- Review third-party integrations for security risks before adoption

### 10. Audit and Monitoring
- Log security-relevant events (authentication, access control changes, data exports)
- Maintain audit trails for agent actions that access or modify sensitive data
- Regularly review logs for suspicious activity
- Implement alerting for potential security breaches
- Conduct regular security assessments and penetration testing

## Enforcement
This rule should trigger whenever:
- Handling credentials, API keys, or sensitive data
- Accessing external systems or APIs
- Storing or retrieving data from memory
- Processing user inputs
- Generating outputs that may contain sensitive information
- Integrating with external services

## Expected Behavior
Agents must operate with security-first mindset, treating all data as sensitive until proven otherwise. Never compromise security for convenience. Follow defense-in-depth principles with multiple layers of protection.
