# Binary Search

## What is it?
Instead of checking every element O(n), binary search cuts the search space in **half** each time → O(log n).

**Only works on sorted arrays.**

## When to use
- Array is sorted
- Searching for a specific value or boundary
- Problem says O(log n) time
- You need to find the first/last position of something
- Finding minimum/maximum value that satisfies a condition ("binary search on the answer")

## The Template — memorize this
```python
left = 0
right = len(array) - 1

while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        left = mid + 1   # target is in right half
    else:
        right = mid - 1  # target is in left half

return -1  # not found
```

## while l <= r vs while l < r — IMPORTANT

**Use `while l <= r`** when:
- You return **inside** the loop (like `return mid`)
- Using `r = mid - 1` and `l = mid + 1` (always shrinks by at least 1)

**Use `while l < r`** when:
- You return **after** the loop (like `return nums[l]`)
- Using `r = mid` (not `mid - 1`) — because `r = mid` with `l <= r` causes infinite loop when `l == r`

**Simple rule:**
- `r = mid - 1` → use `while l <= r`
- `r = mid`     → use `while l < r`

**Why:**
```
# r = mid with l <= r → infinite loop!
l=2, r=2, mid=2 → r=mid=2 → l=2, r=2 → loops forever ✗

# r = mid with l < r → stops correctly
l=2, r=2 → l < r is False → loop ends ✓
```

## 2D Matrix — flatten to 1D
For a matrix with m rows and n columns, treat it as a flat array of size m*n:
```python
m = len(matrix)
n = len(matrix[0])
l = 0
r = m * n - 1

mid = (l + r) // 2
row = mid // n    # which row
col = mid % n     # which column
value = matrix[row][col]
```

## ceil (ceiling division)
When you need to round UP after division:
```python
import math
math.ceil(7 / 4)        # = 2  (easiest, most readable)

(7 + 4 - 1) // 4        # = 2  (integer math, no import)
-(-7 // 4)              # = 2  (double negative trick)
```

Use ceil when calculating hours/steps: `math.ceil(pile / speed)`

## How to think about it
- `mid` recalculates automatically every iteration based on new left and right
- Move `left` right when target is **bigger** than mid
- Move `right` left when target is **smaller** than mid
- Loop ends when `left > right` (or `left == right` for `l < r` variant)

## Key insight
Each iteration eliminates **half** the remaining elements. That's why it's O(log n).

## Common variations
- Find exact value → standard template, return inside loop
- Find insert position → return `l` after loop when not found
- Search in 2D matrix → flatten with `row = mid//n, col = mid%n`
- Binary search on answer → search space is value range, not array indices
- Rotated sorted array → compare `nums[mid]` with `nums[r]` to find which half has minimum
