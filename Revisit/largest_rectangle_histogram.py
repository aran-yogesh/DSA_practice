# ============================================================
# 84. Largest Rectangle in Histogram
# Difficulty: Hard
# Status: REVISIT — logic understood partially, needs more practice
#
# Problem:
# Given an array of integers heights representing histogram bar
# heights (width=1), return the area of the largest rectangle.
#
# Example 1:
#   Input:  heights = [2,1,5,6,2,3]
#   Output: 10  (bars at index 2,3 with height 5, width 2)
#
# Example 2:
#   Input:  heights = [2,4]
#   Output: 4
# ============================================================

# ---- Core Idea ----
# For each bar, the largest rectangle it can be part of extends
# left and right as long as all bars are at least as tall as it.
# A shorter bar is the TRIGGER — it means all taller bars behind
# it can no longer extend right, so calculate their areas now.
#
# Use a monotonic increasing stack. When current bar is shorter
# than stack top → pop and calculate area.
# Store (start_index, height) tuples so we can track how far
# left each bar can extend.


# ---- My Solution ----
def largestRectangleArea_mine(heights):
    stack = []    # stores (start_index, height)
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index           # extend left boundary
        stack.append((start, h))

    # remaining bars in stack never found a shorter bar on the right
    for start, height in stack:
        max_area = max(max_area, height * (len(heights) - start))

    return max_area


# ---- Alternative Solution (better runtime) ----
def largestRectangleArea_optimized(heights):
    res = 0
    stack = [(-1, -1)]
    heights.append(-1)
    prev_h = heights[0]

    for i in range(1, len(heights)):
        h = heights[i]
        if h > prev_h:
            stack.append((i - 1, prev_h))
            prev_h = h
            continue
        if h == prev_h:
            continue
        while h < prev_h:
            cur_h = prev_h
            prev_i, prev_h = stack.pop()
            area = (i - prev_i - 1) * cur_h
            if area > res:
                res = area
        stack.append((prev_i, prev_h))
        prev_h = h
    return res


# ============================================================
# Dry Run: heights = [2,1,5,6,2,3]
#
# i=0 h=2 → stack empty → push (0,2)     stack=[(0,2)]
# i=1 h=1 → 2>1 → pop(0,2), area=2*(1-0)=2, start=0
#          → stack empty → push (0,1)     stack=[(0,1)]
# i=2 h=5 → 1<5 → push (2,5)             stack=[(0,1),(2,5)]
# i=3 h=6 → 5<6 → push (3,6)             stack=[(0,1),(2,5),(3,6)]
# i=4 h=2 → 6>2 → pop(3,6), area=6*(4-3)=6, start=3
#          → 5>2 → pop(2,5), area=5*(4-2)=10 ← MAX!, start=2
#          → 1<2 → stop, push (2,2)       stack=[(0,1),(2,2)]
# i=5 h=3 → 2<3 → push (5,3)             stack=[(0,1),(2,2),(5,3)]
#
# Remaining in stack:
#   (5,3) → area = 3*(6-5) = 3
#   (2,2) → area = 2*(6-2) = 8
#   (0,1) → area = 1*(6-0) = 6
#
# max_area = 10 ✓
#
# Time Complexity:  O(n) — each bar pushed and popped at most once
# Space Complexity: O(n) — stack
# ============================================================

# ---- Where I Needed Assistance ----
# 1. Visualizing the problem — hard to see how area=10 comes from bars 5,6
#    Fix: for each bar, find how far left/right it can extend at its height
#
# 2. Stack condition heights[stack[-1]] > heights[i] — confused what this means
#    Fix: "is the bar at top of stack taller than current bar?"
#    If yes → current bar blocks it from going right → calculate area now
#
# 3. Width calculation — didn't understand i - index
#    Fix: width = current index - start index of the popped bar
#
# 4. start = index inside while loop — didn't understand why
#    Fix: when a taller bar is popped, current bar can extend to where it started
#
# 5. Remaining bars after loop — forgot bars left in stack need area calculated
#    Fix: bars left in stack never hit a shorter bar, so they extend to the end
#
# ---- What to Improve ----
# - This is a HARD problem. Come back after solving more monotonic stack problems.
# - Key pattern: shorter bar = trigger to calculate areas of all taller bars behind it
# - Always store (index, height) tuples when you need both position and value
# - Practice: Next Greater Element, Daily Temperatures first, then revisit this


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([1, 1], 1),
    ]

    print("My Solution:")
    for heights, expected in test_cases:
        output = largestRectangleArea_mine(heights[:])
        print(f"Input: {heights} → Output: {output} | Expected: {expected} | Pass: {output == expected}")

    print()
    print("Optimized Solution:")
    for heights, expected in test_cases:
        output = largestRectangleArea_optimized(heights[:])
        print(f"Input: {heights} → Output: {output} | Expected: {expected} | Pass: {output == expected}")
