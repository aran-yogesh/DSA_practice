# ============================================================
# 42. Trapping Rain Water
# Difficulty: Hard
#
# Problem:
# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water
# it can trap after raining.
#
# Example 1:
#   Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6
#
# Example 2:
#   Input:  height = [4,2,0,3,2,5]
#   Output: 9
# ============================================================

# ---- Strategy: Two Pointers with running max ----
# For any position i, water it can hold =
#     min(max_left, max_right) - height[i]
#
# Use two pointers from both ends, tracking the running max
# on each side. Whichever side has the smaller max is the
# bottleneck — process that side and move inward.
#
# Key insight: water is trapped by the TALLEST wall on each
# side, NOT the nearest neighbour.


def trap(height):
    l = 0
    r = len(height) - 1
    max_left = 0
    max_right = 0
    result = 0

    while l < r:
        max_left = max(max_left, height[l])   # tallest wall seen from left
        max_right = max(max_right, height[r]) # tallest wall seen from right

        if max_left < max_right:
            # left side is the bottleneck, calculate water here
            result += max_left - height[l]
            l += 1
        else:
            # right side is the bottleneck, calculate water here
            result += max_right - height[r]
            r -= 1

    return result


# ============================================================
# Dry Run: height = [4,2,0,3,2,5]
#
# l=0, r=5, max_left=0, max_right=0, result=0
#
# Step 1: l=0, r=5
#   max_left  = max(0,4) = 4
#   max_right = max(0,5) = 5
#   4 < 5 → process left: result += 4-4 = 0 → result=0, l=1
#
# Step 2: l=1, r=5
#   max_left  = max(4,2) = 4
#   max_right = max(5,5) = 5
#   4 < 5 → process left: result += 4-2 = 2 → result=2, l=2
#
# Step 3: l=2, r=5
#   max_left  = max(4,0) = 4
#   max_right = max(5,5) = 5
#   4 < 5 → process left: result += 4-0 = 4 → result=6, l=3
#
# Step 4: l=3, r=5
#   max_left  = max(4,3) = 4
#   max_right = max(5,5) = 5
#   4 < 5 → process left: result += 4-3 = 1 → result=7, l=4
#
# Step 5: l=4, r=5
#   max_left  = max(4,2) = 4
#   max_right = max(5,5) = 5
#   4 < 5 → process left: result += 4-2 = 2 → result=9, l=5
#
# l == r → stop
# Result: 9 ✓
#
# Time Complexity:  O(n) — single pass with two pointers
# Space Complexity: O(1) — no extra data structures
# ============================================================

# ---- Self Reflection: Where I got stuck ----
# 1. Initial logic — was comparing immediate neighbours (i and i+1)
#    instead of the tallest walls on both sides.
#    Key fix: water level = min(max_left, max_right) - height[i]
#    Immediate neighbours don't matter — the TALLEST surrounding walls do.
#
# 2. Why start from both ends — thought we could just loop i and i+1.
#    Key fix: water at any position depends on walls far away, not just
#    next door. Starting from both ends lets us track the running max
#    on each side efficiently.
#
# 3. Understanding the bottleneck — whichever side has the smaller
#    max wall is the limiting factor. Process that side first.
#
# ---- What to improve ----
# - Before coding, visualize the problem with a small example.
#   Ask: "what determines water at position i?"
# - Practice dry runs on paper before jumping to code.
# - The pattern here is the same as Container With Most Water —
#   two pointers, move the limiting side inward.
# - Progress: coded 80-90% independently, only needed help with
#   the core insight. Keep pushing on the "why" behind each step.


if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
    ]

    for height in test_cases:
        print(f"Input:  {height}")
        print(f"Output: {trap(height)}")
        print()
