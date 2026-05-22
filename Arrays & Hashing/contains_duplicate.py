# ============================================================
# 217. Contains Duplicate
# Difficulty: Easy
#
# Problem:
# Given an integer array nums, return true if any value appears
# at least twice, and false if every element is distinct.
#
# Example 1:
#   Input:  nums = [1, 2, 3, 1]
#   Output: True
#
# Example 2:
#   Input:  nums = [1, 2, 3, 4]
#   Output: False
# ============================================================

# ---- Strategy: Set comparison ----
# A set only stores unique values. If the set is smaller than
# the original array, there must be duplicates.


def containsDuplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    return False


# ============================================================
# Dry Run: nums = [1, 2, 3, 1]
#
# len(nums)     = 4
# len(set(nums)) = 3  (set is {1, 2, 3})
# 4 != 3 → return True ✓
#
# Time Complexity:  O(n) — building the set
# Space Complexity: O(n) — storing the set
# ============================================================


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
    ]

    for nums in test_cases:
        print(f"Input:  {nums}")
        print(f"Output: {containsDuplicate(nums)}")
        print()
