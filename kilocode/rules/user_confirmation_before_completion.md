---
name: User Confirmation Before Completion
globs: "**/*"
alwaysApply: true
description: Ensure that the agent always seeks user confirmation before attempting to complete a task
---

# User Confirmation Before Completion

## Purpose
Ensure that the agent always seeks user confirmation before attempting to complete a task, preventing premature completion attempts without user approval.

## Requirements

### 1. Pre-Completion Verification
- Always ask the user for permission before using the attempt_completion tool
- Confirm that the user is satisfied with the work done before attempting to close the task
- Allow users to request additional work or clarifications before completion

### 2. Explicit Consent Protocol
- Before marking any task as complete, explicitly ask: "Do you want me to attempt to complete this task now?"
- Only proceed with attempt_completion after receiving clear affirmative consent from the user
- If the user requests additional work, perform that work before attempting completion again

### 3. Exception Scenarios
- This rule does not apply when explicitly instructed to provide a summary or final response
- This rule does not apply when the user has explicitly told the agent to complete the task

## Enforcement
This rule should trigger whenever:
- An agent is about to use the attempt_completion tool
- A series of tasks or steps have been completed and the agent considers the job finished
- The agent has provided requested information and believes the task is complete

## Expected Behavior
Always seek user confirmation before attempting completion, ensuring users have the opportunity to request additional work or clarifications before closing the task.