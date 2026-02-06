---
name: Error Handling Strategy
globs: "**/*"
alwaysApply: true
description: Comprehensive error management, resilience patterns, and recovery strategies
---

# Error Handling Strategy

## Purpose
Provide a systematic approach to handling errors, ensuring graceful degradation, maintaining system stability, and enabling effective troubleshooting.

## Requirements

### 1. Error Classification and Hierarchy
- Categorize errors by severity: Critical, Major, Minor, Warning, Info
- Distinguish between:
  - **Transient errors**: Temporary issues that may resolve with retry (network timeouts, rate limits)
  - **Permanent errors**: Issues that won't resolve with retry (invalid input, missing resource)
  - **Data errors**: Corruption, validation failures, schema mismatches
  - **System errors**: Resource exhaustion, infrastructure failures
- Implement appropriate handling strategies for each category

### 2. Fail Fast with Context
- Detect errors as early as possible in the execution flow
- Fail immediately when encountering unrecoverable conditions
- Provide rich error context including:
  - Timestamp and operation being performed
  - Input parameters (sanitized to avoid exposing secrets)
  - System state relevant to the failure
  - Suggested remediation steps when available
- Use clear, actionable error messages that distinguish between user errors and system failures

### 3. Retry Mechanisms with Backoff
- Implement exponential backoff for transient failures (initial delay 1s, multiply by 2, max 3 retries)
- Add jitter to retry delays to prevent thundering herd problems
- Set operation-specific timeout thresholds (typically 30-60 seconds)
- Implement circuit breaker pattern for repeated failures to external services
- Track retry counts and escalate to human intervention after threshold
- Log each retry attempt with increasing detail

### 4. Graceful Degradation
- Design systems to continue operating with reduced functionality when components fail
- Provide fallback mechanisms for critical operations:
  - Use cached data when live data is unavailable
  - Switch to alternative providers or methods
  - Disable non-essential features while maintaining core functionality
- Implement feature flags to quickly disable problematic features
- Communicate degraded state clearly to users with appropriate expectations

### 5. Comprehensive Logging Strategy
- Log all errors with sufficient detail for debugging
- Include in logs:
  - Error type and severity level
  - Stack trace for unexpected exceptions
  - Request/operation context (IDs, timestamps)
  - System metrics (memory, CPU, disk space)
  - User/session identifiers (for tracing, sanitized)
- Use structured logging (JSON format) for machine parsing
- Implement log rotation and retention policies
- Separate error logs from general application logs
- Ensure logs don't contain sensitive data (PII, credentials, tokens)

### 6. Error Recovery and Self-Healing
- Implement automatic recovery for known error conditions:
  - Reconnect logic for dropped connections
  - Resource cleanup and reallocation on exhaustion
  - Configuration reloading for updated settings
- Design idempotent operations to safely retry
- Implement health checks and automatic restart for crashed components
- Use watchdog timers for long-running operations
- Document recovery procedures for manual intervention

### 7. Crisis Management and Rollback
- Establish procedures for handling severe failures:
  - Immediate rollback to last known good state
  - Emergency stop mechanisms (kill switches)
  - Isolation of affected components to prevent cascade failures
  - Notification protocols for on-call personnel
- Maintain versioned backups and snapshots for rapid restoration
- Test rollback procedures regularly
- Define clear escalation paths and decision matrices

### 8. Monitoring and Alerting
- Implement real-time monitoring of error rates and patterns
- Set up alerts for:
  - Error rate thresholds (spike detection)
  - Critical error occurrences
  - System resource exhaustion
  - Service availability degradation
- Use dashboards to visualize error trends and system health
- Correlate errors across distributed components
- Implement OpenTelemetry or similar observability standards

### 9. User-Facing Error Handling
- Present user-friendly error messages that:
  - Explain what went wrong in non-technical language
  - Provide clear next steps or actions the user can take
  - Avoid exposing internal system details or stack traces
  - Include support contact information or reference codes
- Differentiate between user-correctable errors and system issues
- Offer retry options for transient failures
- Provide progress indicators for long-running operations that may fail

### 10. Error Prevention and Testing
- Write unit tests covering error paths and edge cases
- Implement chaos engineering practices to test resilience
- Conduct regular fault injection testing
- Validate error handling in integration tests
- Use static analysis tools to identify potential error sources
- Perform code reviews with focus on error handling completeness
- Document known error conditions and their handling in system documentation

### 11. Data Integrity Protection
- Implement transaction semantics for critical operations
- Use compensating transactions for failed multi-step operations
- Validate data consistency after error recovery
- Implement checksums and integrity checks for persisted data
- Design for eventual consistency in distributed systems
- Maintain audit trails of error events and recovery actions

### 12. Dependency Failure Handling
- Implement timeout and retry logic for all external service calls
- Cache responses to mitigate downstream failures
- Use bulkheads to isolate failures between different external services
- Implement fallback providers for critical dependencies
- Monitor dependency health and circuit break on repeated failures
- Gracefully handle dependency unavailability during startup

## Enforcement
This rule should trigger whenever:
- Writing code that handles errors or exceptions
- Integrating with external services or APIs
- Designing system architecture or workflows
- Implementing retry logic or circuit breakers
- Setting up monitoring and alerting
- Performing testing or disaster recovery planning

## Expected Behavior
Agents should design systems with resilience as a primary concern, anticipating failures and implementing appropriate safeguards. Errors should be treated as opportunities to improve system robustness, not just as exceptions to handle. Always consider: What can fail? What happens when it does? How do we recover?
