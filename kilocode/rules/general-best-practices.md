---
name: General Coding Standards
globs: "**/*.{js,ts,py,go,java,rb,cs}"
alwaysApply: true
description: Universal coding standards applicable across all programming languages
---

# General Coding Standards

## Purpose
To ensure clean, maintainable, and consistent code across all programming languages by applying proven software engineering principles and best practices.

## Requirements

### 1. Naming Conventions
- Use descriptive and meaningful names
- Be consistent with naming patterns
- Avoid abbreviations and single letters (except loop counters)
- Use searchable names for constants
- Make the purpose clear from the name

### 2. Function Design
- Keep functions small and focused (single responsibility)
- Limit function parameters (ideally 3 or fewer)
- Use descriptive function names that indicate action
- Avoid side effects when possible
- Return early to reduce nesting

### 3. Code Organization
- Group related functionality together
- Use consistent file structure
- Separate concerns into modules/classes
- Keep files focused and reasonably sized
- Use clear folder hierarchies

### 4. Error Prevention
- Validate inputs at boundaries
- Use type systems when available
- Handle edge cases explicitly
- Fail fast with clear messages
- Use defensive programming techniques

### 5. Code Readability
- Write code for humans to read
- Use consistent formatting
- Add whitespace for visual separation
- Limit line length (80-120 characters)
- Use meaningful variable names

### 6. DRY Principle
- Don't Repeat Yourself
- Extract common functionality
- Use configuration over duplication
- Create reusable components
- Balance DRY with clarity

### 7. SOLID Principles
- **Single Responsibility**: One reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable
- **Interface Segregation**: Many specific interfaces
- **Dependency Inversion**: Depend on abstractions

### 8. Best Practices
- Prefer composition over inheritance
- Write tests for your code
- Refactor regularly
- Use version control effectively
- Document architectural decisions

## Enforcement
This rule should trigger whenever:
- Writing new code or modifying existing code
- Performing code reviews
- Setting up new projects or modules
- Establishing coding standards for a team
- Refactoring or improving code quality

## Expected Behavior
Agents should apply these standards intuitively to all code they produce. These principles form the foundation of clean code and should be second nature when writing, reviewing, or refactoring code. Always prioritize readability, maintainability, and extensibility.
