# Cross-Platform Command Patterns

Use these patterns when executing file operations on home directory paths (`~/.kilocode/`). All commands use `execute_command` and are grouped by operation type.

---

## Directory Listing

**List all files in a directory:**
```
Unix/Linux/macOS: ls -la ~/.kilocode/path/ 2>/dev/null
Windows cmd.exe: dir %USERPROFILE%\.kilocode\path 2>nul
Windows PowerShell: Get-ChildItem "$HOME\.kilocode\path" -ErrorAction SilentlyContinue
```

**List only markdown files:**
```
Unix/Linux/macOS: ls ~/.kilocode/path/*.md 2>/dev/null
Windows cmd.exe: dir %USERPROFILE%\.kilocode\path\*.md /b 2>nul
Windows PowerShell: Get-ChildItem "$HOME\.kilocode\path" -Filter *.md -ErrorAction SilentlyContinue | Select-Object Name
```

---

## File Reading

**Read entire file:**
```
Unix/Linux/macOS: cat ~/.kilocode/path/filename.md
Windows cmd.exe: type %USERPROFILE%\.kilocode\path\filename.md
Windows PowerShell: Get-Content "$HOME\.kilocode\path\filename.md" -Raw
```

**Read with line numbers (for debugging):**
```
Unix/Linux/macOS: cat -n ~/.kilocode/path/filename.md
Windows cmd.exe: type %USERPROFILE%\.kilocode\path\filename.md | find /n " "
Windows PowerShell: Get-Content "$HOME\.kilocode\path\filename.md" | Select-Object -Index (0..100)
```

---

## Pattern Searching

**Search for pattern in files (case-insensitive):**
```
Unix/Linux/macOS: grep -r "(?i){PATTERN}" ~/.kilocode/path/ 2>/dev/null
Windows cmd.exe: findstr /s /i /m "{PATTERN}" %USERPROFILE%\.kilocode\path\*.md 2>nul
Windows PowerShell: Select-String -Path "$HOME\.kilocode\path\*.md" -Pattern "(?i){PATTERN}" -ErrorAction SilentlyContinue | Select-Object Path
```

**Search and return matching lines with context:**
```
Unix/Linux/macOS: grep -r -C 2 "(?i){PATTERN}" ~/.kilocode/path/ 2>/dev/null
Windows cmd.exe: findstr /s /i /c:"{PATTERN}" %USERPROFILE%\.kilocode\path\*.md 2>nul
Windows PowerShell: Select-String -Path "$HOME\.kilocode\path\*.md" -Pattern "(?i){PATTERN}" -Context 2,2 -ErrorAction SilentlyContinue
```

---

## File Writing

**Write content to file (overwrite):**
```
Unix/Linux/macOS: cat > ~/.kilocode/path/filename.md << 'EOF'
content here
EOF
Windows cmd.exe: echo content > "%USERPROFILE%\.kilocode\path\filename.md"
Windows PowerShell: Set-Content -Path "$HOME\.kilocode\path\filename.md" -Value "content"
```

**Append content to file:**
```
Unix/Linux/macOS: cat >> ~/.kilocode/path/filename.md << 'EOF'
additional content
EOF
Windows cmd.exe: echo additional content >> "%USERPROFILE%\.kilocode\path\filename.md"
Windows PowerShell: Add-Content -Path "$HOME\.kilocode\path\filename.md" -Value "additional content"
```

---

## File Existence Checks

**Check if file exists:**
```
Unix/Linux/macOS: test -f ~/.kilocode/path/filename.md && echo "exists" || echo "missing"
Windows cmd.exe: if exist "%USERPROFILE%\.kilocode\path\filename.md" (echo exists) else (echo missing)
Windows PowerShell: Test-Path "$HOME\.kilocode\path\filename.md" && echo "exists" || echo "missing"
```

**Check if directory exists:**
```
Unix/Linux/macOS: test -d ~/.kilocode/path/ && echo "exists" || echo "missing"
Windows cmd.exe: if exist "%USERPROFILE%\.kilocode\path\" (echo exists) else (echo missing)
Windows PowerShell: Test-Path "$HOME\.kilocode\path" -PathType Container && echo "exists" || echo "missing"
```

---

## Directory Creation

**Create directory (including parents):**
```
Unix/Linux/macOS: mkdir -p ~/.kilocode/path/
Windows cmd.exe: mkdir %USERPROFILE%\.kilocode\path
Windows PowerShell: New-Item -ItemType Directory -Path "$HOME\.kilocode\path" -Force
```

---

## Git Operations

**Search branches by pattern (case-insensitive):**
```
Unix/Linux/macOS: git branch -a | grep -i "{PATTERN}"
Windows cmd.exe: git branch -a | findstr /i "{PATTERN}"
Windows PowerShell: git branch -a | Select-String -Pattern "(?i){PATTERN}"
```

### Sleep / Delay

**Pause execution for N seconds:**
```
Unix/Linux/macOS: sleep 2
Windows cmd.exe: timeout /t 2 /nobreak >nul
Windows PowerShell: Start-Sleep -Seconds 2
```
**Note:** Adjust the duration (e.g., 1-3 seconds) as needed for retry intervals.

### Retry Policy for Transient Failures

When an `execute_command` fails (non-zero exit code), retry up to 2 times with a brief pause (1-3 seconds) between attempts using the sleep patterns above.

Example sequence:
1. Execute command
2. If exit code != 0, sleep for 2 seconds
3. Retry (second attempt)
4. If still fails, sleep for 2 seconds
5. Retry (third attempt)
6. If still fails, report error and ask user: "Command failed after retries. How would you like me to proceed? Retry again, skip this step, or abort?"

This handles transient issues like file locks or temporary network unavailability for mounted drives.


---

## Notes

- Replace `{PATTERN}` with the actual search pattern
- Replace `filename.md` with actual filename
- Replace `path` with actual directory path (e.g., `context`, `plans`, `skills/research/references`)
- On Windows, use `%USERPROFILE%` or `%HOME%` in cmd.exe, or `$HOME` in PowerShell
- On Unix/Linux/macOS, `~` expands automatically in the shell
- Redirect stderr (`2>/dev/null` or `2>nul`) to suppress error messages when files/directories don't exist
- Use `-ErrorAction SilentlyContinue` in PowerShell to suppress errors
