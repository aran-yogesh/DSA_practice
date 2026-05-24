# ============================================================
# 33. Search in Rotated Sorted Array
# Difficulty: Medium
#
# Problem:
# Given a rotated sorted array of unique integers and a target,
# return the index of target if found, or -1 if not found.
# Must run in O(log n) time.
#
# Example 1:
#   Input:  nums = [4,5,6,7,0,1,2], target = 0   Output: 4
# Example 2:
#   Input:  nums = [4,5,6,7,0,1,2], target = 3   Output: -1
# Example 3:
#   Input:  nums = [1], target = 0               Output: -1
# ============================================================

# ---- Strategy: Binary Search with sorted half check ----
# At every mid, one half is always sorted. Check which half is
# sorted, then check if target falls in that sorted half.
#
# If left half sorted (nums[l] <= nums[mid]):
#   - target in [nums[l], nums[mid]) → r = mid - 1
#   - else → l = mid + 1
#
# If right half sorted:
#   - target in (nums[mid], nums[r]] → l = mid + 1
#   - else → r = mid - 1
#
# Use while l <= r because we use mid-1 and mid+1 (always shrinks)


def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:        # left half is sorted
            if nums[l] <= target < nums[mid]:
                r = mid - 1             # target in left half
            else:
                l = mid + 1             # target in right half
        else:                           # right half is sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1             # target in right half
            else:
                r = mid - 1             # target in left half

    return -1


# ============================================================
# Dry Run: nums = [4,5,6,7,0,1,2], target = 0
# l=0, r=6
#
# Step 1: mid=3, nums[3]=7 != 0
#   nums[l]=4 <= nums[mid]=7 → left half sorted
#   target=0 in [4, 7)? No → l=4
#   l=4, r=6
#
# Step 2: mid=5, nums[5]=1 != 0
#   nums[l]=0 <= nums[mid]=1 → left half sorted
#   target=0 in [0, 1)? Yes → r=4
#   l=4, r=4
#
# Step 3: mid=4, nums[4]=0 == 0 → return 4 ✓
#
# Dry Run: nums = [4,5,6,7,0,1,2], target = 3
#
# Step 1: mid=3, nums[3]=7 != 3
#   left sorted, 3 not in [4,7) → l=4
# Step 2: mid=5, nums[5]=1 != 3
#   left sorted, 3 not in [0,1) → l=6
# Step 3: mid=6, nums[6]=2 != 3
#   left sorted, 3 not in [2,2) → l=7
# l=7 > r=6 → return -1 ✓
#
# Time Complexity:  O(log n) — search space halves each step
# Space Complexity: O(1)     — only pointers used
# ============================================================

# ---- Key Insight ----
# In a rotated array, at least ONE half is always sorted.
# Check which half is sorted first, then check if target is in that half.
# This tells you exactly which direction to move.

# ---- Where I Needed Assistance ----
# 1. return mid inside loop — bug, returns after first iteration always
#    Fix: remove it, only return when nums[mid] == target
#
# 2. nums[mid] > r — comparing value with index!
#    Fix: always compare values: nums[mid] vs nums[l] or nums[r]
#
# 3. Core logic — which half is sorted and how to check target in it
#    Fix: if nums[l] <= nums[mid] → left sorted
#         if nums[mid] < target <= nums[r] → right sorted and target in right
#
# 4. while l < r → should be while l <= r
#    Fix: using mid-1 and mid+1 always shrinks → use l <= r
#         l < r misses the last element when l == r
#
# ---- What to Improve ----
# - Rule: mid-1 and mid+1 → use while l <= r
# - Always compare VALUES not indices (nums[l] not l)
# - Rotated array pattern: one half is always sorted — find which one first
# - Check if target is in the sorted half using range comparison


if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
    ]

    for nums, target, expected in test_cases:
        output = search(nums, target)
        print(f"Input:    nums={nums}, target={target}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
