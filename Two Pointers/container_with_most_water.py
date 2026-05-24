# ============================================================
# 11. Container With Most Water
# Difficulty: Medium
#
# Problem:
# Given an integer array height of length n, find two lines
# that together with the x-axis form a container that holds
# the most water. Return the maximum amount of water.
#
# Example 1:
#   Input:  height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#
# Example 2:
#   Input:  height = [1,1]
#   Output: 1
# ============================================================

# ---- Strategy: Two Pointers from both ends ----
# Start with the widest container (l=0, r=end).
# Each iteration calculate area and update max.
# Move the pointer with the SHORTER height inward —
# moving the taller wall can never increase area.


def maxArea(height):
    l = 0
    r = len(height) - 1
    max_area = 0

    while l < r:
        # area = width * height (height is limited by shorter wall)
        max_area = max(max_area, (r - l) * min(height[l], height[r]))

        # move the shorter wall — keeping it can never improve area
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


# ============================================================
# Dry Run: height = [1,8,6,2,5,4,8,3,7]
#
# l=0, r=8 → area = 8 * min(1,7) = 8  → max=8,  move l (height 1 < 7)
# l=1, r=8 → area = 7 * min(8,7) = 49 → max=49, move r (height 7 < 8)
# l=1, r=7 → area = 6 * min(8,3) = 18 → max=49, move r (height 3 < 8)
# l=1, r=6 → area = 5 * min(8,8) = 40 → max=49, move r (tie → r-=1)
# l=1, r=5 → area = 4 * min(8,4) = 16 → max=49, move r
# l=1, r=4 → area = 3 * min(8,5) = 15 → max=49, move r
# l=1, r=3 → area = 2 * min(8,2) = 4  → max=49, move r
# l=1, r=2 → area = 1 * min(8,6) = 6  → max=49, move r
# l=1, r=1 → l == r, stop
#
# Result: 49 ✓
#
# Time Complexity:  O(n) — single pass with two pointers
# Space Complexity: O(1) — no extra data structures
# ============================================================

# ---- Tradeoffs ----
# This approach (two pointers, greedy):
#   O(n) time, O(1) space — optimal
#   The greedy choice (always move shorter wall inward) is provably correct
#
# Brute force (check every pair):
#   O(n²) time, O(1) space — too slow for large inputs
#
# There is no O(n log n) middle ground — you either check all pairs O(n²)
# or use the greedy insight O(n). Two pointers is the only efficient solution.

# ---- Self Reflection: Where I got stuck ----
# 1. Area formula — thought it was squaring the second largest number.
#    Key insight: area = width * height, height = min(left, right wall)
#
# 2. Updating max — was overwriting max_area every iteration.
#    Fix: use max(max_area, new_area) to always keep the biggest
#
# 3. Pointer condition — compared indices (r > l) instead of heights.
#    Fix: always compare height[l] vs height[r], not the indices
#
# 4. When to stop — loop naturally stops when l == r, no extra logic needed
#
# General rule for two pointer problems: ask yourself —
#   - What do I calculate each iteration?
#   - How do I track the best result?
#   - Which pointer moves and based on what condition?


if __name__ == "__main__":
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [4, 3, 2, 1, 4],
    ]

    for height in test_cases:
        print(f"Input:  {height}")
        print(f"Output: {maxArea(height)}")
        print()
