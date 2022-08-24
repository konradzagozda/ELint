# ELint
Elastic Python + language agnostic linter with rule definition capabilities



# CLI:

```elint <dir> --conf=<path>```

# Use case example:
we don't want pytz so we could define rule:
```
RULES = [
    {
        'rule-name':'illegal-pytz',
        'files-pattern': '*.py',
        'illegal-statements': ['from pytz', 'import pytz', 'pytz'],
        'filepaths-to-exclude': ['must-use-pytz-in-this-file.py', 'app-that-uses-pytz-directory'],
        'root-dir': 'backend | frontend | project root'
     }
]
```
