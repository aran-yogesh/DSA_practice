# Arrays & Hashing

## What is it?
Using arrays and hashmaps (dictionaries) to store, count, and look up data efficiently.

## When to use
- Counting frequency of elements
- Checking if something exists (O(1) lookup)
- Grouping elements by a common property
- Finding pairs or complements

## Key Data Structures

### Dictionary (Hashmap)
```python
d = {}
d[key] = value       # store
d[key] += 1          # increment
if key in d:         # check existence O(1)
    print(d[key])    # lookup O(1)
```

### Set
```python
s = set()
s.add(x)       # add element
x in s         # check existence O(1) — faster than list!
```

## How to think about it
Before coding a hashmap always ask:
1. **What is the key?** — what am I looking up by?
2. **What is the value?** — what information do I need to store?

## Common Patterns
- **Counting:** `map[x] = map.get(x, 0) + 1`
- **Complement lookup:** store seen values, check `target - x`
- **Grouping:** use sorted string or tuple as key
- **Duplicate detection:** compare `len(nums)` vs `len(set(nums))`

## Complexities
- Hashmap lookup/insert: O(1) average
- Set lookup: O(1) average
- Building hashmap from array: O(n)
