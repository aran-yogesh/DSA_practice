# ============================================================
# 155. Min Stack
# Difficulty: Medium
#
# Problem:
# Design a stack that supports push, pop, top, and retrieving
# the minimum element in constant time O(1).
#
# Example:
#   MinStack minStack = new MinStack()
#   minStack.push(-2)
#   minStack.push(0)
#   minStack.push(-3)
#   minStack.getMin() → -3
#   minStack.pop()
#   minStack.top()    → 0
#   minStack.getMin() → -2
# ============================================================

# ---- Strategy: Store tuples (value, current_min) ----
# Each element is stored as a tuple: (value, min_at_this_point)
# When pushing, track the minimum so far by comparing val
# with the current min at the top of the stack.
# getMin() just returns the second element of the top tuple.


class MinStack:

    def __init__(self):
        self.st = []           # stores tuples of (value, current_min)

    def push(self, val: int) -> None:
        mini = val
        if self.st:
            mini = min(mini, self.st[-1][1])   # compare with current min
        self.st.append((val, mini))            # store value AND min together

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]                  # first element of tuple

    def getMin(self) -> int:
        return self.st[-1][1]                  # second element of tuple = min


# ============================================================
# Dry Run: push(-2), push(0), push(-3), getMin, pop, top, getMin
#
# push(-2): st=[(-2,-2)]          min so far = -2
# push(0):  st=[(-2,-2),(0,-2)]   min so far = -2 (0 > -2)
# push(-3): st=[(-2,-2),(0,-2),(-3,-3)]  min so far = -3
# getMin → st[-1][1] = -3 ✓
# pop    → st=[(-2,-2),(0,-2)]
# top    → st[-1][0] = 0 ✓
# getMin → st[-1][1] = -2 ✓
#
# Time Complexity:  O(1) — all operations are constant time
# Space Complexity: O(n) — storing n tuples for n pushes
# ============================================================

# ---- Tradeoffs ----
# This approach (store tuples (value, current_min)):
#   O(1) all operations, O(n) space
#   Pro: Single structure — no sync issues; min is always one index away
#   Con: Stores redundant min values even when min doesn't change
#
# Two-stack alternative:
#   One stack for values, one for min values (push to min stack only on new minimum)
#   Same O(1) operations; slightly less space in practice
#   Con: Two structures to maintain — must keep them in sync on every pop
#
# Both are valid; tuple approach is simpler to reason about

# ---- Self Reflection: Where I got stuck ----
# 1. Class structure — unsure how to initialise variables and
#    which self variables to use. Key: always init in __init__
#    with self.variable = starting value.
#
# 2. getMin in O(1) — initially unclear how to track min without
#    looping. Fix: store the current min alongside each value as
#    a tuple so every element remembers the min at its push time.
#
# 3. Accessing tuple elements — self.st[-1][0] for value,
#    self.st[-1][1] for min. Index into the tuple just like a list.
#
# ---- What to improve ----
# - Practice writing class-based solutions — init, self, methods.
# - When a problem asks for O(1) on something that changes,
#   think about storing extra info alongside each element.
# - Tuple trick: (value, extra_info) is a common stack pattern.


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"getMin: {minStack.getMin()}")  # -3
    minStack.pop()
    print(f"top:    {minStack.top()}")     # 0
    print(f"getMin: {minStack.getMin()}")  # -2
