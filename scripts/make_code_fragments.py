"""
This is a simple helper script to prepare fragments for highlighting
from code blocks.
"""
block = """
git status
git apply patches/modify_files_and_add_new_file.md
git status
git diff
git add training/file*.md
git diff
git diff --staged
git commit -m "Modified file1 and file2 and added file3.md"
git log -n2 --oneline
"""

fragment = """
::: {{.fragment .current-only data-code-focus="{}"}}
```{{bash}}
#| echo: false
{}
```
:::"""

counter = 0
for line in block.split("\n"):
    if line.strip():
        counter += 1
        print(fragment.format(counter, line))
