# ============================================================
# 739. Daily Temperatures
# Difficulty: Medium
#
# Problem:
# Given an array of integers temperatures, return an array
# answer where answer[i] is the number of days to wait after
# day i to get a warmer temperature. If no warmer day exists,
# answer[i] = 0.
#
# Example 1:
#   Input:  temperatures = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
#
# Example 2:
#   Input:  temperatures = [30,40,50,60]
#   Output: [1,1,1,0]
#
# Example 3:
#   Input:  temperatures = [30,60,90]
#   Output: [1,1,0]
# ============================================================

# ---- Strategy: Monotonic Stack ----
# Store INDICES of days that haven't found a warmer day yet.
# For each day, check if it's warmer than days sitting in the stack.
# If yes → pop those days and fill in their answer (i - j).
# If no  → push current index and wait.
#
# Key insight: store indices (not temperatures) so you can
# calculate the difference between days directly.


def dailyTemperatures(temperatures):
    stack = []                          # stores indices waiting for warmer day
    answer = [0] * len(temperatures)   # default 0 for days with no warmer day

    for i, temp in enumerate(temperatures):
        # pop all days that are colder than today
        while stack and temp > temperatures[stack[-1]]:
            j = stack.pop()             # index of the colder day
            answer[j] = i - j          # days waited = today's index - that day's index
        stack.append(i)                 # push today's index, still waiting for warmer day

    return answer


# ============================================================
# Dry Run: temperatures = [73,74,75,71,69,72,76,73]
#          answer starts = [0, 0, 0, 0, 0, 0, 0, 0]
#
# i=0, temp=73 → stack empty → push 0       → stack=[0]
# i=1, temp=74 → 74>temps[0]=73 → pop 0, answer[0]=1-0=1 → push 1  → stack=[1]
# i=2, temp=75 → 75>temps[1]=74 → pop 1, answer[1]=2-1=1 → push 2  → stack=[2]
# i=3, temp=71 → 71<temps[2]=75 → push 3                            → stack=[2,3]
# i=4, temp=69 → 69<temps[3]=71 → push 4                            → stack=[2,3,4]
# i=5, temp=72 → 72>temps[4]=69 → pop 4, answer[4]=5-4=1
#              → 72>temps[3]=71 → pop 3, answer[3]=5-3=2
#              → 72<temps[2]=75 → stop, push 5                       → stack=[2,5]
# i=6, temp=76 → 76>temps[5]=72 → pop 5, answer[5]=6-5=1
#              → 76>temps[2]=75 → pop 2, answer[2]=6-2=4
#              → stack empty, push 6                                  → stack=[6]
# i=7, temp=73 → 73<temps[6]=76 → push 7                            → stack=[6,7]
#
# answer = [1,1,4,2,1,1,0,0] ✓
#
# Time Complexity:  O(n) — each index pushed and popped at most once
# Space Complexity: O(n) — stack can hold up to n indices
# ============================================================

# ---- Tradeoffs ----
# This approach (monotonic stack):
#   O(n) time, O(n) space — each index pushed and popped at most once
#   Pro: Optimal time complexity
#
# Brute force (nested loops):
#   For each day scan forward to find the next warmer day → O(n²) time, O(1) space
#   Too slow for large inputs
#
# The O(n) space cost is unavoidable — unresolved days must be remembered
# somewhere until a future warmer day arrives. Stack is the right structure
# because resolution order is unpredictable (LIFO matches when a big day resolves many)

# ---- Self Reflection: Where I got stuck ----
# 1. Visualizing the problem — kept thinking two pointers.
#    Fix: this is NOT two pointers. You need a stack because each
#    element is waiting for a future element — unknown how far ahead.
#
# 2. What to store in stack — tried storing temperatures.
#    Fix: store INDICES so you can calculate i - j for the answer.
#
# 3. Indentation of stack.append(i) — put it inside while loop.
#    Fix: append AFTER the while loop. You push current index once,
#    not every time you pop.
#
# 4. Using while loop instead of if — needed the while to pop
#    multiple waiting days at once when a much warmer day arrives.
#
# ---- What to improve ----
# - Monotonic stack pattern: use when you need "next greater element"
#   for each position. Stack stores indices of unresolved elements.
# - Always ask: what am I storing in the stack — value or index?
#   If you need to calculate distance/position, store the index.
# - while stack and condition → pop until stack empty or condition fails.
#   This is the core monotonic stack pattern.


if __name__ == "__main__":
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ]

    for temperatures, expected in test_cases:
        output = dailyTemperatures(temperatures)
        print(f"Input:    {temperatures}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
