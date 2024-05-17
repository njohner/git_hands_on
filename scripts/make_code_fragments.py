"""
This is a simple helper script to prepare fragments for highlighting
from code blocks.
"""
block = """
git log -n5 --oneline --graph --decorate --all
git rebase temp
git log -n5 --oneline --graph --decorate --all
git checkout temp
git merge dev
git log -n5 --oneline --graph --decorate --all
git branch -d dev
"""

fragment = """
::: {{.fragment .current-only data-code-focus="{i}" fragment-index={i}}}
```{{bash}}
#| echo: false
{code}
```
:::"""

counter = 0
for line in block.split("\n"):
    if line.strip():
        counter += 1
        print(fragment.format(i=counter, code=line))
