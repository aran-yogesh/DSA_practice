# ============================================================
# 167. Two Sum II - Input Array Is Sorted
# Difficulty: Medium
#
# Problem:
# Given a 1-indexed sorted array of integers, find two numbers
# such that they add up to target. Return their indices
# (1-indexed) as [index1, index2].
#
# You must use only constant extra space.
#
# Example 1:
#   Input:  numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]
#
# Example 2:
#   Input:  numbers = [2, 3, 4], target = 6
#   Output: [1, 3]
#
# Example 3:
#   Input:  numbers = [-1, 0], target = -1
#   Output: [1, 2]
# ============================================================

# ---- Strategy: Two Pointers ----
# Since the array is sorted, use two pointers (l, r):
#   - If sum == target → return indices
#   - If sum > target  → move r left (make sum smaller)
#   - If sum < target  → move l right (make sum bigger)
# No extra space needed — O(1) space!


def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        total = numbers[l] + numbers[r]

        if total == target:
            return [l + 1, r + 1]  # 1-indexed output
        elif total > target:
            r -= 1  # sum too big, move right pointer left
        else:
            l += 1  # sum too small, move left pointer right


# ============================================================
# Dry Run: numbers = [2, 7, 11, 15], target = 9
#
# l=0, r=3 → 2 + 15 = 17 → too big  → r=2
# l=0, r=2 → 2 + 11 = 13 → too big  → r=1
# l=0, r=1 → 2 +  7 =  9 → found!   → return [1, 2]
#
# Time Complexity:  O(n) — single pass with two pointers
# Space Complexity: O(1) — no extra data structures
# ============================================================


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
    ]

    for numbers, target in test_cases:
        print(f"Input:  numbers={numbers}, target={target}")
        print(f"Output: {twoSum(numbers, target)}")
        print()
