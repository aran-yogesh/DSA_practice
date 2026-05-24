# ============================================================
# 4. Median of Two Sorted Arrays
# Difficulty: Hard
# Status: REVISIT — merge solution works, binary search too hard
#         for now. Come back after more binary search practice.
#
# Problem:
# Given two sorted arrays nums1 and nums2 of size m and n,
# return the median of the two sorted arrays.
# Must run in O(log(m+n)) time.
#
# Example 1:
#   Input:  nums1 = [1,3], nums2 = [2]
#   Output: 2.0
#
# Example 2:
#   Input:  nums1 = [1,2], nums2 = [3,4]
#   Output: 2.5
# ============================================================

# ---- My Working Solution — O(m+n) ----
# Merge the two sorted arrays using two pointers (like merge sort),
# then find the median from the merged array.

from typing import List


def findMedianSortedArrays_merge(nums1: List[int], nums2: List[int]) -> float:
    m = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            m.append(nums1[i])
            i += 1
        else:
            m.append(nums2[j])
            j += 1

    m.extend(nums1[i:])
    m.extend(nums2[j:])

    n = len(m)
    if n % 2 == 1:
        return float(m[n // 2])
    else:
        return (m[n // 2 - 1] + m[n // 2]) / 2


# ============================================================
# Time Complexity:  O(m+n) — merging both arrays
# Space Complexity: O(m+n) — the merged array
# ============================================================

# ---- Binary Search Approach — O(log(m+n)) — TO REVISIT ----
#
# Core idea: don't merge. Instead binary search for the correct
# PARTITION across both arrays simultaneously.
#
# Key concepts understood so far:
#
# half = (len(nums1) + len(nums2) + 1) // 2
#   → how many elements belong on the LEFT side of the median
#   → the +1 handles both odd and even total lengths cleanly
#
# Binary search only on nums1 (the smaller array):
#   cut1 = mid          → nums1 contributes cut1 elements to the left
#   cut2 = half - cut1  → nums2's cut is FORCED from cut1
#
# At each step, check 4 boundary values:
#   left1  = nums1[cut1 - 1]   (last element on left of nums1)
#   right1 = nums1[cut1]       (first element on right of nums1)
#   left2  = nums2[cut2 - 1]   (last element on left of nums2)
#   right2 = nums2[cut2]       (first element on right of nums2)
#
# Valid partition when:
#   left1 <= right2  AND  left2 <= right1
#
# If left1 > right2 → cut1 is too far right → move l left
# If left2 > right1 → cut1 is too far left  → move l right
#
# Handle edge cases with float('inf') and float('-inf')
# when cut is at the boundary of an array.
#
# Final answer:
#   Odd total  → max(left1, left2)
#   Even total → (max(left1, left2) + min(right1, right2)) / 2
#
# ---- Why it's hard ----
# - Requires visualising two cuts at once
# - Edge cases at array boundaries need -inf / +inf guards
# - The partition logic is non-obvious until you've seen it many times
#
# ---- What to do before revisiting ----
# - Get comfortable with: Find Minimum in Rotated Array
# - Get comfortable with: Search in Rotated Sorted Array
# - Then come back — the partition concept will click faster


if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ]

    print("Merge Solution:")
    for nums1, nums2, expected in test_cases:
        output = findMedianSortedArrays_merge(nums1[:], nums2[:])
        print(f"nums1={nums1}, nums2={nums2} → {output} | Expected: {expected} | Pass: {output == expected}")
