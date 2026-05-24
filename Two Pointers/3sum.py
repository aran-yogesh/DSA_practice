# ============================================================
# 15. 3Sum
# Difficulty: Medium
#
# Problem:
# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that:
#   - i != j, i != k, j != k
#   - nums[i] + nums[j] + nums[k] == 0
#
# The solution set must not contain duplicate triplets.
#
# Example 1:
#   Input:  nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1, -1, 2], [-1, 0, 1]]
#
# Example 2:
#   Input:  nums = [0, 1, 1]
#   Output: []
#
# Example 3:
#   Input:  nums = [0, 0, 0]
#   Output: [[0, 0, 0]]
# ============================================================

# ---- Strategy: Sort + Fix One + Two Pointers ----
# 1. Sort the array
# 2. Fix one number nums[i] with a loop
# 3. Use two pointers (l, r) on the rest to find pairs that sum to -nums[i]
# 4. Skip duplicates for i to avoid duplicate triplets


def threeSum(nums):
    nums = sorted(nums)  # sort so two pointers work correctly
    ans = []

    for i in range(len(nums)):
        # skip duplicate values for the fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif total > 0:
                r -= 1  # sum too big, move right pointer left
            else:
                l += 1  # sum too small, move left pointer right

    return ans


# ============================================================
# Dry Run: nums = [-1, 0, 1, 2, -1, -4]
#
# After sorting: [-4, -1, -1, 0, 1, 2]
#
# i=0, nums[i]=-4, l=1, r=5
#   -4 + -1 + 2 = -3 → too small → l+=1
#   -4 + -1 + 2 = -3 → too small → l+=1
#   -4 +  0 + 2 = -2 → too small → l+=1
#   -4 +  1 + 2 = -1 → too small → l+=1
#   l == r → stop
#
# i=1, nums[i]=-1, l=2, r=5
#   -1 + -1 + 2 = 0 → found! append [-1,-1,2], l+=1, r-=1
#   -1 +  0 + 1 = 0 → found! append [-1, 0,1], l+=1, r-=1
#   l == r → stop
#
# i=2, nums[i]=-1 → same as nums[i-1]=-1 → skip!
#
# i=3, nums[i]=0, l=4, r=5
#   0 + 1 + 2 = 3 → too big → r-=1
#   l == r → stop
#
# Result: [[-1,-1,2], [-1,0,1]] ✓
#
# Time Complexity:  O(n²) — one loop + two pointers inside
# Space Complexity: O(n)  — output array
# ============================================================

# ---- Tradeoffs ----
# This approach (sort + fix one + two pointers):
#   Pro: Clean duplicate-skipping using sorted order; O(n²) is optimal here
#
# HashSet alternative (fix nums[i], use set for pairs):
#   Same O(n²) time but duplicate handling is messy without sorting
#   Con: Harder to deduplicate correctly
#
# Brute force (three nested loops):
#   O(n³) time — too slow; never use for large inputs
#
# Sorting is the key unlock: makes duplicates adjacent and enables two pointers


if __name__ == "__main__":
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
    ]

    for nums in test_cases:
        print(f"Input:  {nums}")
        print(f"Output: {threeSum(nums)}")
        print()
