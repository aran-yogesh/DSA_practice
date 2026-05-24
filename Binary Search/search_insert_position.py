# ============================================================
# 35. Search Insert Position
# Difficulty: Easy
#
# Problem:
# Given a sorted array of distinct integers and a target,
# return the index if found. If not, return the index where
# it would be inserted in order. Must run in O(log n).
#
# Example 1:
#   Input:  nums = [1,3,5,6], target = 5  → Output: 2
# Example 2:
#   Input:  nums = [1,3,5,6], target = 2  → Output: 1
# Example 3:
#   Input:  nums = [1,3,5,6], target = 7  → Output: 4
# ============================================================

# ---- Strategy: Binary Search ----
# Same as standard binary search. The only difference:
# when target is NOT found, return l instead of -1.
# When the loop ends, l always lands at the correct insert position.
#
# Key insight: l ends up at the first number BIGGER than target
# which is exactly where target should be inserted.


def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid          # found — return index
        elif nums[mid] > target:
            r = mid - 1         # target in left half
        else:
            l = mid + 1         # target in right half

    return l                    # not found — l is the insert position


# ============================================================
# Dry Run: nums = [1,3,5,6], target = 2
#
# Start: l=0, r=3
#
# Step 1: mid=(0+3)//2=1 → nums[1]=3 > 2 → r=mid-1=0
#         l=0, r=0
#
# Step 2: mid=(0+0)//2=0 → nums[0]=1 < 2 → l=mid+1=1
#         l=1, r=0
#
# l=1 > r=0 → loop ends → return l=1 ✓
# (2 belongs at index 1, where 3 currently sits)
#
# Dry Run: nums = [1,3,5,6], target = 7
#
# Step 1: mid=1 → nums[1]=3 < 7 → l=2
# Step 2: mid=3 → nums[3]=6 < 7 → l=4
# l=4 > r=3 → return l=4 ✓ (insert at end)
#
# Time Complexity:  O(log n) — search space halves each step
# Space Complexity: O(1)     — only three pointers
# ============================================================

# ---- Key Insight ----
# When target is not found, l always ends up at the first number
# that is BIGGER than target — exactly where target should be inserted.
#
# Why:
# - l moves right when nums[mid] < target → skipping smaller numbers
# - l stops when it hits something bigger than target
# - That position = insert position
# So just return l — no extra logic needed!

# ---- Tradeoffs ----
# This approach (binary search, return l when not found):
#   O(log n) time, O(1) space — optimal
#   Pro: No extra logic after the loop — l naturally lands at the insert position
#
# Linear scan alternative:
#   Loop through to find where target fits → O(n) time, O(1) space
#   Simple to understand but too slow for large sorted arrays
#
# Key insight: "return l" instead of "return -1" is the only change from
# standard binary search. l always ends at the first element > target.

# ---- Where I Needed Assistance ----
# 1. while l < r vs while l <= r
#    Fix: must use <= otherwise loop ends too early when l==r
#    and we miss the last element check
#
# 2. r = mid vs r = mid - 1 (and l = mid vs l = mid + 1)
#    Fix: without +1/-1, when l==r==mid nothing changes → infinite loop!
#    Always shrink by 1 to guarantee progress each iteration.
#
# 3. What to return when target not found
#    Fix: return l not -1. l naturally lands at the insert position
#    after the loop ends.
#
# 4. Visualizing where mid goes
#    Fix: mid recalculates every iteration as (l+r)//2.
#    It doesn't "move" — it recomputes based on new l and r.
#
# ---- What to Improve ----
# - Always use while l <= r for binary search (not l < r)
# - Always use mid+1 and mid-1 (never just mid) to avoid infinite loops
# - For "insert position" problems: return l when not found
# - Dry run on paper with small arrays to see l, r, mid move


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 1, 0),
    ]

    for nums, target, expected in test_cases:
        output = searchInsert(nums, target)
        print(f"Input:    nums={nums}, target={target}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
