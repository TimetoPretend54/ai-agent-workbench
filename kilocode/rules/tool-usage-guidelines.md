---
name: Tool Usage Guidelines
globs: "**/*"
alwaysApply: true
description: Best practices for using available tools effectively and safely
---

# Tool Usage Guidelines

## Purpose
Ensure consistent, efficient, and safe usage of available tools (execute_command, edit_file, write_to_file, read_file, etc.) to maintain code quality and prevent errors.

## Requirements

### 1. Tool Selection Principles
- Choose the right tool for the job:
  - `read_file`: View existing file contents (read-only)
  - `edit_file`: Make targeted changes to existing files (preferred for modifications)
  - `write_to_file`: Create new files or completely replace existing files
  - `apply_diff`: Apply precise surgical changes with exact matching
  - `execute_command`: Run CLI commands or scripts
  - `search_files`: Find patterns across files
  - `list_files`: Explore directory structure
- Prefer `edit_file` over `write_to_file` for modifications to preserve file integrity
- Use `apply_diff` only when you need exact, multi-location changes with precise matching

### 2. Pre-Operation Validation
- Check file existence before attempting to read or edit
- Verify file paths are correct relative to workspace root
- Validate that operations are idempotent (safe to retry)
- Confirm write permissions before file modifications
- Check disk space for large operations

### 3. File Modification Safety
- Always read a file before editing to understand current state
- Use `edit_file` with sufficient context (3+ lines before/after) for uniqueness
- Avoid overwriting files unless explicitly intended
- Create backups before destructive operations (use version control if available)
- Preserve file formatting, line endings, and encoding
- Validate file changes after editing

### 4. Command Execution Best Practices
- Test commands in a safe environment before production use
- Use absolute paths or properly resolved relative paths
- Add error handling and exit code checks
- Log command output for debugging
- Avoid interactive commands unless explicitly required
- Use appropriate shell syntax for the target OS (cmd.exe vs bash vs PowerShell)
- Set reasonable timeouts for long-running operations

### 5. Idempotency and Retry Logic
- Design operations to be idempotent (safe to repeat)
- Implement retry mechanisms with exponential backoff (max 3 retries)
- Check operation results before proceeding
- Handle partial failures gracefully
- Clean up temporary files and resources after operations

### 6. Error Handling Strategy
- Capture and log all error messages
- Distinguish between fatal and recoverable errors
- Provide meaningful error context in logs
- Fail fast with clear messages for unrecoverable errors
- Implement fallback mechanisms when appropriate
- Report errors to users with actionable information

### 7. Resource Management
- Monitor memory usage during large file operations
- Close file handles promptly after operations
- Clean up temporary files and processes
- Avoid loading entire large files into memory when possible
- Use streaming for large data transfers
- Implement progress indicators for long-running operations

### 8. Cross-Platform Compatibility
- Use platform-agnostic commands when possible
- Handle path separators correctly (forward slash works on Windows too)
- Be aware of OS-specific limitations (command availability, file locking)
- Test commands on target platforms
- Use environment variables for platform detection (`%USERPROFILE%` vs `$HOME`)

### 9. Search and Discovery
- Use specific, targeted search patterns
- Limit search scope to relevant directories
- Combine multiple search criteria when needed
- Use file pattern filters to improve performance
- Review search results in context before acting

### 10. List Operations
- Use `list_files` to explore unfamiliar directories
- Prefer non-recursive listing for top-level exploration
- Use recursive listing only when necessary (can be slow)
- Check for symlinks and special files
- Respect directory boundaries (don't traverse outside workspace)

### 11. Change Management
- Make small, focused changes rather than large sweeping modifications
- Group related changes logically
- Document significant changes in comments or commit messages
- Review changes before finalizing
- Use version control to track modifications

### 12. Tool Chain Optimization
- Combine related operations to reduce tool calls
- Cache results of expensive operations when appropriate
- Minimize data transfer between tools
- Use batch operations when supported
- Avoid redundant tool invocations

## Enforcement
This rule should trigger whenever:
- Using any tool or API
- Performing file operations
- Executing commands
- Searching or listing files
- Making changes to the codebase
- Interacting with external systems

## Expected Behavior
Agents should use tools thoughtfully and efficiently, always considering safety, performance, and maintainability. Choose the simplest tool that accomplishes the task, and always validate operations before and after execution.
