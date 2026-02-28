# Engineering Principles

This document defines the core engineering principles that all skills must enforce to ensure solid, maintainable, and secure designs.

## 1. DRY (Don't Repeat Yourself)

**Definition**: Avoid duplication of code, patterns, and configuration. Reuse existing components, utilities, and design tokens.

**Enforcement**:
- Search for existing patterns before creating new ones
- Leverage shared components and libraries
- Extract common functionality into reusable utilities
- Use established design tokens and styling systems

**Verification**:
- Plan identifies all reusable elements
- No unnecessary duplication of logic or components
- Clear rationale when duplication is unavoidable

## 2. Scalability

**Definition**: Design systems that handle growth in data volume, user load, feature complexity, and team size without degradation.

**Enforcement**:
- Evaluate performance implications of design choices
- Consider phased implementation for larger features
- Document capacity limits and scaling thresholds
- Identify potential bottlenecks early (database, network, compute)
- Plan for horizontal/vertical scaling where appropriate

**Verification**:
- Performance characteristics documented
- Load testing strategy included (if applicable)
- Caching, load balancing, or sharding strategies identified
- Growth scenarios considered and addressed

## 3. Architectural Risk Analysis

**Definition**: Proactively identify and mitigate risks arising from dependencies, coupling, and system interactions.

**Enforcement**:
- Analyze dependencies for version compatibility
- Trace data sources and ownership
- Identify tight coupling and single points of failure
- Evaluate blast radius of changes
- Document backward compatibility requirements

**Verification**:
- All external dependencies listed with versions
- Risks explicitly documented with mitigation strategies
- Compatibility constraints clearly stated
- Rollback or degradation paths identified

## 4. Operational & Reliability Considerations

**Definition**: Ensure systems can be monitored, maintained, and recovered from failures with minimal downtime.

**Enforcement**:
- Document failure modes and recovery procedures
- Define observability requirements (logs, metrics, traces)
- Plan for graceful degradation
- Establish health checks and alerting
- Document operational runbooks

**Verification**:
- Key failure scenarios identified
- Monitoring and alerting coverage defined
- Recovery time objectives (RTO) and recovery point objectives (RPO) considered
- Runbook documentation included

## 5. Security & Safety Baseline

**Definition**: Protect against threats, ensure data privacy, and establish safe usage boundaries.

**Enforcement**:
- Identify data exposure risks (PII, credentials, secrets)
- Validate external dependencies for trust and vulnerabilities
- Review authentication and authorization requirements
- Define safe defaults and configuration boundaries
- Document assumptions about trust boundaries

**Verification**:
- Security risks documented with mitigations
- Secrets management approach defined
- Input validation and sanitization requirements stated
- Dependency trust assessment completed
- Safe usage boundaries clearly communicated

## 6. Testability & Change Safety

**Definition**: Design systems that can be validated and evolved with confidence through comprehensive testing and change isolation.

**Enforcement**:
- Identify testing seams and mocking points
- Define unit, integration, and end-to-end test coverage goals
- Evaluate blast radius of changes
- Plan for feature flags or canary deployments
- Document regression testing requirements

**Verification**:
- Test strategy documented (unit, integration, e2e)
- Test examples provided for critical paths
- Change isolation mechanisms identified
- Regression test coverage planned
- Validation approach for each deliverable defined

---

**Usage**: All skills should reference these principles in their quality checklists and enforce them through their respective steps.