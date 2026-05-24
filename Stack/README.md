# Stack

## What is it?
A data structure that works like a stack of plates — you can only add or remove from the top. **Last In, First Out (LIFO).**

## When to use
- Matching pairs (brackets, tags)
- Tracking previous state / undo operations
- Next greater/smaller element problems
- Evaluating expressions

## In Python — stack is just a list
```python
stack = []

stack.append(x)   # push — add to top
stack.pop()       # pop  — remove and return top
stack[-1]         # peek — see top without removing
len(stack) == 0   # check if empty
not stack         # same as above
```

## Monotonic Stack
A stack kept in sorted order (increasing or decreasing).
Use when you need "next greater/smaller element" for each position.

### Template
```python
stack = []   # stores indices

for i in range(len(arr)):
    while stack and condition(arr[stack[-1]], arr[i]):
        j = stack.pop()
        # resolve answer for j using i
    stack.append(i)

# anything left in stack has no resolution → default answer (0)
```

### When to use Monotonic Stack
- "Next greater element" for each position
- "How many days until warmer temperature"
- "Largest rectangle" type problems
- Result for each element depends on a future element

## Key Tips
- Always check if stack is empty before popping: `if not stack or ...`
- After the loop, elements left in stack = unresolved (use default answer)
- Store **indices** not values when you need position/distance calculation
- Never return True/False prematurely inside a loop

## Complexities
- Push/pop/peek: O(1)
- Monotonic stack full pass: O(n) — each element pushed and popped at most once
