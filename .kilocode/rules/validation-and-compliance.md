# Validation and Compliance Rule

## Purpose
Ensure that all tasks are validated through actual testing rather than assumptions, and that user instructions are followed precisely.

## Requirements

### 1. Manual Testing Requirement
- When asked to "test" functionality, perform actual validation steps
- Do not make assumptions about whether something works without verification
- For workflow testing, attempt to execute or validate the actual functionality

### 2. User Instruction Compliance
- Follow user instructions exactly as given
- When user says "you didn't do anything", acknowledge and take corrective action
- Prioritize user feedback over assumptions about completeness

### 3. Validation Before Completion
- Validate that requested functionality actually works before marking as complete
- Test the actual commands/processes mentioned in the request
- Confirm functionality through direct interaction, not inference

### 4. Assumption Prevention
- Do not assume system states or functionality without verification
- Question assumptions and validate through testing
- When uncertain about functionality, explicitly test it

## Enforcement
This rule should trigger whenever:
- A user requests testing of functionality
- A user indicates that work was not completed
- Making claims about system functionality without validation
- Closing tasks without proper verification

## Expected Behavior
Always validate through testing, follow user instructions precisely, and ensure actual functionality works before claiming completion.