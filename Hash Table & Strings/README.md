# Hash Table & Strings

## What is it?
Combining string manipulation with hashmap lookups to solve character/pattern based problems efficiently.

## When to use
- Converting between representations (Roman numerals, etc.)
- Character counting and comparison
- Pattern matching
- Substring problems

## Key String Operations
```python
s.lower()          # lowercase
s.isalnum()        # check if alphanumeric
s[::-1]            # reverse string
"".join(list)      # join list into string
sorted(s)          # sort characters → returns list
"".join(sorted(s)) # sort characters → returns string
```

## Key Hashmap Pattern for Strings
```python
d = {}
for c in s:
    d[c] = d.get(c, 0) + 1   # count character frequency
```

## How to think about it
- When comparing two strings → think about character frequency
- When converting → predefine a lookup dictionary
- When checking boundaries → always guard against index out of range with `i + 1 < len(s)`

## Common Patterns
- **Anagram check:** compare frequency hashmaps or sorted strings
- **Subtraction rule:** if current value < next value → subtract (Roman numerals)
- **Sliding window:** expand right, shrink left when condition breaks

## Key Tips
- `i + 1 < len(s)` — always check before accessing `s[i+1]`
- Dictionary with fixed known keys = O(1) space
- `Counter` from collections is a shortcut for frequency counting
