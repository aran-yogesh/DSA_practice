# ============================================================
# 1. Two Sum
# Difficulty: Easy
#
# Problem:
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.
#
# Example 1:
#   Input:  nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
#
# Example 2:
#   Input:  nums = [3, 2, 4], target = 6
#   Output: [1, 2]
# ============================================================

# ---- Strategy: Hashmap (one pass) ----
# For each number, calculate its complement (target - num).
# If complement already exists in the hashmap, return both indices.
# Otherwise store the current number and its index.


def twoSum(nums, target):
    seen = {}  # key: number, value: index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


# ============================================================
# Dry Run: nums = [2, 7, 11, 15], target = 9
#
# i=0, num=2  → complement=7,  not in seen → seen={2:0}
# i=1, num=7  → complement=2,  found at index 0 → return [0,1] ✓
#
# Time Complexity:  O(n) — single pass
# Space Complexity: O(n) — hashmap stores up to n elements
# ============================================================

# ---- Tradeoffs ----
# This approach (hashmap, one pass):
#   Pro: O(n) time — optimal for unsorted input
#   Con: O(n) extra space for the hashmap
#
# Alternative 1 — Brute force:
#   Check every pair → O(n²) time, O(1) space — too slow for large inputs
#
# Alternative 2 — Sort + two pointers:
#   Sort array, use l/r pointers → O(n log n) time, O(1) space
#   Con: Sorting destroys original indices (needed for the output here)
#   Only valid when the problem asks for values, not indices


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]

    for nums, target in test_cases:
        print(f"Input:  nums={nums}, target={target}")
        print(f"Output: {twoSum(nums, target)}")
        print()
