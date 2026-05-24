# ============================================================
# 704. Binary Search
# Difficulty: Easy
#
# Problem:
# Given an array of integers nums sorted in ascending order,
# and an integer target, return the index of target if found,
# or -1 if not found. Must run in O(log n) time.
#
# Example 1:
#   Input:  nums = [-1,0,3,5,9,12], target = 9
#   Output: 4
#
# Example 2:
#   Input:  nums = [-1,0,3,5,9,12], target = 2
#   Output: -1
# ============================================================

# ---- Strategy: Binary Search ----
# Use left and right pointers to define the search boundary.
# Calculate mid each iteration. Shrink the boundary based on
# whether target is greater or less than nums[mid].
# Each iteration cuts the search space in half → O(log n).


def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid          # found it — return index
        elif nums[mid] < target:
            l = mid + 1         # target is in right half
        else:
            r = mid - 1         # target is in left half

    return -1                   # not found


# ============================================================
# Dry Run: nums = [-1,0,3,5,9,12], target = 9
#
# l=0, r=5, mid=2 → nums[2]=3  < 9  → l=3
# l=3, r=5, mid=4 → nums[4]=9 == 9  → return 4 ✓
#
# Dry Run: nums = [-1,0,3,5,9,12], target = 2
#
# l=0, r=5, mid=2 → nums[2]=3  > 2  → r=1
# l=0, r=1, mid=0 → nums[0]=-1 < 2  → l=1
# l=1, r=1, mid=1 → nums[1]=0  < 2  → l=2
# l=2 > r=1 → loop ends → return -1 ✓
#
# Time Complexity:  O(log n) — search space halves each iteration
# Space Complexity: O(1)     — only three pointers used
# ============================================================

# ---- Self Reflection: Where I got stuck ----
# 1. Variable naming — used l and r but wrote left and right inside loop.
#    Fix: be consistent — pick one and stick with it throughout.
#
# 2. Return value — returned nums[mid] (the value) instead of mid (the index).
#    Fix: always re-read what the problem asks to return — value or index?
#
# ---- What to improve ----
# - Memorize the template: while l <= r, mid = (l+r)//2, l=mid+1, r=mid-1
# - Key decision: nums[mid] < target → move l right, nums[mid] > target → move r left
# - mid recalculates automatically each iteration — it doesn't "move", it recomputes


if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], 3, -1),
    ]

    for nums, target, expected in test_cases:
        output = search(nums, target)
        print(f"Input:    nums={nums}, target={target}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
