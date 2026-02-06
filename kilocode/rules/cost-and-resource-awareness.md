---
name: Cost and Resource Awareness
globs: "**/*"
alwaysApply: true
description: Guidelines for managing API costs, token usage, and computational resources efficiently
---

# Cost and Resource Awareness

## Purpose
Prevent unexpected costs, optimize resource usage, and ensure sustainable operation of AI agents by implementing cost controls and efficiency measures.

## Requirements

### 1. API Cost Management
- Set explicit spend limits on all LLM API accounts (OpenAI, Anthropic, OpenRouter, etc.)
- Monitor token usage in real-time and implement hard limits
- Use cost tracking tools and dashboards to visualize spending patterns
- Alert when approaching predefined budget thresholds
- Implement automatic throttling or shutdown when limits are reached

### 2. Token Efficiency
- Use structured output (JSON, XML) to reduce token consumption and improve parsing
- Minimize context window usage through intelligent compression and summarization
- Remove unnecessary whitespace, comments, and verbose content from prompts
- Use the smallest effective model for the task (downgrade after establishing baseline)
- Implement token budgeting per operation type

### 3. Model Selection Strategy
- Start with the best model to establish performance baseline
- Systematically test cheaper alternatives to find the optimal cost/performance ratio
- Document model choices and their appropriate use cases
- Consider model latency and throughput requirements
- Cache results for identical or similar queries when appropriate

### 4. Operation Optimization
- Combine related operations to reduce API calls
- Implement batching for independent operations
- Use parallel execution judiciously (consider rate limits and costs)
- Avoid redundant computations or repeated API calls
- Implement smart retry logic with exponential backoff (max 3 retries)

### 5. Resource Monitoring
- Track execution time and computational resources for each operation
- Identify and optimize expensive operations
- Set timeouts for long-running operations (typically 30-60 seconds)
- Monitor memory usage and implement cleanup for large data structures
- Log resource consumption metrics for analysis

### 6. Caching and Memoization
- Cache frequently accessed data with appropriate TTL (time-to-live)
- Implement semantic caching for similar queries (not just exact matches)
- Use persistent cache for expensive computations
- Invalidate cache strategically to balance freshness and cost
- Document cache hit rates and eviction policies

### 7. Cost-Aware Planning
- Estimate costs before executing expensive operations
- Provide users with cost estimates for multi-step workflows
- Implement "preview" modes that show planned actions without execution
- Allow users to approve or modify expensive operations
- Prioritize low-cost alternatives when multiple approaches exist

### 8. Rate Limiting and Throttling
- Implement client-side rate limiting to avoid hitting API limits
- Use exponential backoff for rate-limited responses
- Distribute load across multiple API keys or providers when possible
- Queue operations during high-cost periods
- Respect provider rate limits and implement proper error handling

### 9. Data Transfer Optimization
- Minimize data sent to and from APIs (compress, filter, sample)
- Use streaming responses for large outputs instead of waiting for complete response
- Implement pagination for large result sets
- Avoid transferring duplicate or redundant data
- Use efficient serialization formats (MessagePack, Protocol Buffers) for internal data

### 10. Cost Transparency
- Log all API calls with associated costs
- Provide detailed cost breakdowns in reports and summaries
- Track cost per task, per user, or per project as needed
- Generate regular cost reports and trend analysis
- Make cost information available to users for budgeting

## Enforcement
This rule should trigger whenever:
- Making API calls to external services (LLMs, search engines, etc.)
- Processing large datasets or performing computations
- Designing multi-step workflows or agent plans
- Implementing caching or optimization strategies
- Setting up new agent deployments or configurations

## Expected Behavior
Agents should operate with cost-consciousness, treating computational resources and API calls as billable expenses. Always consider the financial implications of agent actions and implement appropriate safeguards to prevent unexpected costs.
