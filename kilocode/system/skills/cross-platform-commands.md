# Cross-Platform Command Patterns

Use these patterns when checking for existing work.

---

## Plan / Context File Detection

Mac / Linux:
ls ~/.kilocode/plans/ 2>/dev/null | grep -i "{PATTERN}"
ls ~/.kilocode/context/ 2>/dev/null | grep -i "{PATTERN}"

Windows (PowerShell):
Get-ChildItem "$HOME\.kilocode\plans" -ErrorAction SilentlyContinue | Select-String "{PATTERN}"
Get-ChildItem "$HOME\.kilocode\context" -ErrorAction SilentlyContinue | Select-String "{PATTERN}"

---

## Git Branch Detection

Mac / Linux:
git branch -a | grep -i "{PATTERN}"

Windows (PowerShell):
git branch -a | Select-String -Pattern "{PATTERN}"
