# ============================================================
# 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
#
# Problem:
# Given a sorted rotated array of unique elements, return the
# minimum element. Must run in O(log n) time.
#
# Example 1:
#   Input:  nums = [3,4,5,1,2]     Output: 1
# Example 2:
#   Input:  nums = [4,5,6,7,0,1,2] Output: 0
# Example 3:
#   Input:  nums = [11,13,15,17]   Output: 11
# ============================================================

# ---- Strategy: Binary Search on rotated array ----
# Compare nums[mid] with nums[r] to decide which half has the minimum:
#   - If nums[mid] > nums[r] → minimum is in the RIGHT half → l = mid + 1
#   - If nums[mid] <= nums[r] → minimum is in the LEFT half (or mid itself) → r = mid
#
# Use while l < r (not l <= r) because r = mid (not mid-1)
# When l == r, both point to the minimum → return nums[l]


def findMin(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1     # minimum is in right half
        else:
            r = mid         # minimum is in left half or mid itself

    return nums[l]


# ============================================================
# Dry Run: nums = [4,5,6,7,0,1,2]
# l=0, r=6
#
# Step 1: mid=3 → nums[3]=7 > nums[6]=2 → minimum in right → l=4
#         l=4, r=6
#
# Step 2: mid=5 → nums[5]=1 <= nums[6]=2 → minimum in left → r=5
#         l=4, r=5
#
# Step 3: mid=4 → nums[4]=0 <= nums[5]=1 → minimum in left → r=4
#         l=4, r=4
#
# l == r → loop ends → return nums[4] = 0 ✓
#
# Dry Run: nums = [3,4,5,1,2]
# l=0, r=4
#
# Step 1: mid=2 → nums[2]=5 > nums[4]=2 → l=3
# Step 2: mid=3 → nums[3]=1 <= nums[4]=2 → r=3
# l=3, r=3 → return nums[3] = 1 ✓
#
# Time Complexity:  O(log n) — search space halves each step
# Space Complexity: O(1)     — only pointers used
# ============================================================

# ---- Key Insight ----
# Compare nums[mid] with nums[r] to find which half is "broken":
#   - If nums[mid] > nums[r] → the rotation point is in the right half
#   - If nums[mid] <= nums[r] → the left half is the broken side, mid could be min
#
# Simple solution min(nums) works but is O(n) — binary search gives O(log n)

# ---- Tradeoffs ----
# This approach (binary search, compare mid with r):
#   O(log n) time, O(1) space — optimal
#   Pro: Converges cleanly; comparing with r (not l) is the key for rotated arrays
#
# min(nums) alternative:
#   Python built-in → O(n) time, O(1) space — one line but fails O(log n) requirement
#
# Find-pivot-then-index alternative:
#   Binary search for the rotation index, then return nums[pivot]
#   Same O(log n) time but more thought required — this approach is cleaner
#
# Why compare with nums[r] and not nums[l]:
#   nums[mid] > nums[r] → rotation point is in the right half (min is there)
#   nums[mid] <= nums[r] → left half is sorted or mid is the min

# ---- Where I Needed Assistance ----
# 1. Which half has the minimum — compare nums[mid] with nums[r]
#    If nums[mid] > nums[r] → right half has minimum
#    If nums[mid] <= nums[r] → left half (or mid) has minimum
#
# 2. r = mid vs r = mid - 1:
#    Use r = mid because mid itself could be the minimum
#    Using r = mid - 1 would skip it!
#
# 3. while l < r vs while l <= r:
#    Use l < r because r = mid (not mid - 1)
#    r = mid with l <= r causes infinite loop when l == r == mid
#
# 4. What to return — return nums[l] after loop (l == r == answer)
#
# ---- What to Improve ----
# - Rule: r = mid → use while l < r. r = mid-1 → use while l <= r
# - For rotated arrays: always compare mid with r (not l) to find which half is sorted
# - When loop ends with l < r variant, l and r are equal and point to the answer


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
        ([2, 1], 1),
    ]

    for nums, expected in test_cases:
        output = findMin(nums)
        print(f"Input:    {nums}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
