# Plan Template for New Assignment

# {ASSIGNMENT_NUMBER}: {Title}

## Overview
{1-2 sentence summary}

## Prerequisites
- [ ] {Dependency 1} - Status: ✅/⏳/🚧
- [ ] {Dependency 2} - Status: ✅/⏳/🚧

## Data Sources
| Field | Source | Notes |
|-------|--------|-------|
| {field} | API / Config / Context | {details} |

## Mock Strategy
| What  | Mock?  | Notes |
|-------|--------|-------|
| {API/Service} | Yes/No | {details} |

## Implementation Phases

### Phase 1: {Name}
- [ ] {Task with file path}
- [ ] {Task with file path}

### Phase 2: {Name}
- [ ] {Task with file path}

## Files
| Action | Path |
|--------|------|
| CREATE | `path/to/new/file` |
| MODIFY | `path/to/existing/file` |

## Testing
- [ ] Unit tests: `{test command}`
- [ ] Manual test: `{scenario}`

## AC Verification
| AC | Covered | Notes |
|----|---------|-------|
| {AC item} | ✅/❌ | {where} |

## 🚧 Mock Cleanup
- [ ] Delete: `path/to/mock/file`
- [ ] Remove mock code in `path/to/file`

## Quick Start for New Code Agent / Task
**Context:** `~/.agents/context/{TOPIC}.context.md`
**First:** Create/modify `path/to/first/file`  
**Order:** Phase 1 -> Phase 2 -> ...  
**Test:** `{test command}`
