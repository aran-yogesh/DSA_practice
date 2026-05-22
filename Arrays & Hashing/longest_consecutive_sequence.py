# ============================================================
# 128. Longest Consecutive Sequence
# Difficulty: Medium
#
# Problem:
# Given an unsorted array of integers nums, return the length
# of the longest consecutive elements sequence. Must run O(n).
#
# Example 1:
#   Input:  nums = [2, 20, 4, 10, 3, 4, 5]
#   Output: 4  (sequence: 2, 3, 4, 5)
#
# Example 2:
#   Input:  nums = [0, 3, 2, 5, 4, 6, 1, 1]
#   Output: 7  (sequence: 0, 1, 2, 3, 4, 5, 6)
# ============================================================

# ---- Strategy: Set + sequence start detection ----
# Put all numbers in a set for O(1) lookup.
# A number is the START of a sequence if num-1 is NOT in the set.
# From each start, count how far the sequence goes using while loop.


def longestConsecutive(nums):
    s = set(nums)  # convert to set to remove duplicates and get O(1) lookup
    out = 0

    for num in s:  # loop over set to avoid processing duplicates
        if num - 1 not in s:  # num is the start of a sequence
            length = 1
            while num + length in s:  # count how long the sequence goes
                length += 1
            out = max(out, length)  # keep track of longest

    return out


# ============================================================
# Dry Run: nums = [2, 20, 4, 10, 3, 4, 5]
# s = {2, 3, 4, 5, 10, 20}
#
# num=2:  2-1=1 not in s → sequence start!
#         2+1=3 in s → length=2
#         2+2=4 in s → length=3
#         2+3=5 in s → length=4
#         2+4=6 not in s → stop, out=4
#
# num=3:  3-1=2 in s → not a start, skip
# num=4:  4-1=3 in s → not a start, skip
# num=5:  5-1=4 in s → not a start, skip
# num=10: 10-1=9 not in s → sequence start, length=1, out stays 4
# num=20: 20-1=19 not in s → sequence start, length=1, out stays 4
#
# Result: 4 ✓
#
# Time Complexity:  O(n) — each number is visited at most twice
# Space Complexity: O(n) — the set
# ============================================================


if __name__ == "__main__":
    test_cases = [
        [2, 20, 4, 10, 3, 4, 5],
        [0, 3, 2, 5, 4, 6, 1, 1],
        [100, 4, 200, 1, 3, 2],
    ]

    for nums in test_cases:
        print(f"Input:  {nums}")
        print(f"Output: {longestConsecutive(nums)}")
        print()
