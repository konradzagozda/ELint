RULES = [
    {
        'rule-name':'illegal-pytz',
        'illegal-statements': ['from pytz', 'import pytz', 'pytz'],
        'filepaths-to-exclude': ['must-use-pytz-in-this-file.py', 'app-that-uses-pytz-directory'],
     }
]