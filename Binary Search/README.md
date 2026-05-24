# Binary Search

## What is it?
Instead of checking every element O(n), binary search cuts the search space in **half** each time → O(log n).

**Only works on sorted arrays.**

## When to use
- Array is sorted
- Searching for a specific value or boundary
- Problem says O(log n) time
- You need to find the first/last position of something

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

## How to think about it
- `mid` recalculates automatically every iteration based on new left and right
- Move `left` right when target is **bigger** than mid
- Move `right` left when target is **smaller** than mid
- Loop ends when `left > right` — search space is exhausted

## Key insight
Each iteration eliminates **half** the remaining elements. That's why it's O(log n).

## Common variations
- Find exact value → standard template above
- Find leftmost position → keep going after finding target
- Find rightmost position → keep going after finding target
- Search in rotated array → check which half is sorted first
