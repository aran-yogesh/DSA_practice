# Sliding Window

## What is it?
Instead of recalculating everything from scratch each step, maintain a **window** that slides across the array — adding from the right, removing from the left.

Without sliding window: O(n²) — recalculate every subarray
With sliding window: O(n) — just update the edges

**Only works on contiguous subarrays or substrings.**

## When to use
- "Longest/shortest subarray or substring that satisfies X"
- "Subarray of size k" (fixed window)
- "No repeating characters / at most k distinct" (variable window)
- Any time you're scanning a contiguous chunk

---

## Type 1 — Fixed Size Window

Window size `k` is given. Slide it one step at a time, tracking something inside.

```
nums = [1, 2, 3, 4, 5]   k=3
[1, 2, 3]
   [2, 3, 4]
      [3, 4, 5]
```

### Template
```python
window_sum = sum(nums[:k])    # build first window
best = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i]      # add new right element
    window_sum -= nums[i - k]  # remove old left element
    best = max(best, window_sum)

return best
```

### Key rule
- `nums[i]` — new element entering from the right
- `nums[i - k]` — old element leaving from the left
- No need for l and r pointers — just use index math

---

## Type 2 — Variable Size Window

Window grows and shrinks based on a condition. Size is not fixed.

```
l=0                    r expands →
[a, b, c, d, e, f]
     ← l shrinks when condition breaks
```

### Template
```python
l = 0
seen = set()   # or dict, or counter — depends on problem
best = 0

for r in range(len(nums)):
    # 1. add nums[r] to window
    seen.add(nums[r])

    # 2. shrink from left while window is invalid
    while window is invalid:
        seen.remove(nums[l])
        l += 1

    # 3. update best — window is always valid here
    best = max(best, r - l + 1)

return best
```

### Key rules
- `r` moves right **every** iteration — always expanding
- `l` moves right **only** when window breaks — shrinking
- Use `while` not `if` — one removal may not be enough to fix the window
- Window size = `r - l + 1`

---

## r - l + 1 explained

```
s = "a b c"
     0 1 2

l=0, r=2 → elements: a(0), b(1), c(2) → 3 elements
r - l + 1 = 2 - 0 + 1 = 3 ✓

r - l alone = 2 ✗ (off by one — misses the element at l)
```

The `+1` is always needed when counting indices inclusive on both ends.

---

## What to track inside the window

| Problem type | Track with |
|---|---|
| No repeating chars | `set` |
| At most k distinct chars | `dict` (char → count) |
| Sum / average | running `int` variable |
| Max / min | `deque` (monotonic) |

---

## Problems solved
| # | Problem | Type | Difficulty |
|---|---|---|---|
| 3   | Longest Substring Without Repeating Characters | Variable | Medium |
| 121 | Best Time to Buy and Sell Stock               | Variable | Easy   |
| 424 | Longest Repeating Character Replacement       | Variable | Medium |
| 567 | Permutation in String                         | Fixed    | Medium |
