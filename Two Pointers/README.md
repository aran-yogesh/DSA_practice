# Two Pointers

## What is it?
Using two variables (pointers) to traverse an array from different positions simultaneously, avoiding nested loops.

## When to use
- Array is sorted
- Finding pairs or triplets that sum to a target
- Comparing elements from both ends
- Removing duplicates in place
- Sliding window problems

## The Template
```python
left = 0
right = len(array) - 1

while left < right:
    # do something with array[left] and array[right]
    if condition:
        left += 1
    else:
        right -= 1
```

## How to think about it
- Always ask: **which pointer moves and why?**
- Move the pointer that is the **bottleneck** (shorter wall, smaller value)
- Moving the larger side can never improve the result

## Common Patterns
- **Sum too big** → move right pointer left
- **Sum too small** → move left pointer right
- **Found match** → move both pointers inward
- **Skip duplicates** → check `if nums[i] == nums[i-1]: continue`

## Key Tips
- For 3Sum: sort first, fix one element with outer loop, use two pointers for the rest
- Always handle duplicates when the problem says "unique" results
- Two pointers = O(n), nested loops = O(n²) — always prefer two pointers on sorted arrays

## Complexities
- Time: O(n) for single pass
- Space: O(1) — no extra data structures needed
