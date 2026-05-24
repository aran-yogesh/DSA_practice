# ============================================================
# 238. Product of Array Except Self
# Difficulty: Medium
#
# Problem:
# Given an integer array nums, return an array answer such that
# answer[i] is the product of all elements except nums[i].
# Must run in O(n) time without using division.
#
# Example 1:
#   Input:  nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
#
# Example 2:
#   Input:  nums = [-1, 1, 0, -3, 3]
#   Output: [0, 0, 9, 0, 0]
# ============================================================

# ---- Strategy: Prefix and Suffix products ----
# answer[i] = product of everything LEFT of i
#           * product of everything RIGHT of i
#
# Pass 1 (left to right):  build left products array
# Pass 2 (right to left):  build right products array
# Pass 3: multiply left[i] * right[i] for each position


def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n   # left[i]  = product of all elements before i
    right = [1] * n  # right[i] = product of all elements after i
    answer = []

    # build left products
    running = 1
    for i in range(n):
        left[i] = running
        running *= nums[i]

    # build right products
    running = 1
    for i in range(n - 1, -1, -1):
        right[i] = running
        running *= nums[i]

    # multiply left and right for each index
    for i in range(n):
        answer.append(left[i] * right[i])

    return answer


# ============================================================
# Dry Run: nums = [1, 2, 3, 4]
#
# Left products (store before multiplying current):
#   i=0: left[0]=1,  running=1*1=1
#   i=1: left[1]=1,  running=1*2=2
#   i=2: left[2]=2,  running=2*3=6
#   i=3: left[3]=6,  running=6*4=24
#   left = [1, 1, 2, 6]
#
# Right products (store before multiplying current):
#   i=3: right[3]=1,  running=1*4=4
#   i=2: right[2]=4,  running=4*3=12
#   i=1: right[1]=12, running=12*2=24
#   i=0: right[0]=24, running=24*1=24
#   right = [24, 12, 4, 1]
#
# answer = [1*24, 1*12, 2*4, 6*1] = [24, 12, 8, 6] ✓
#
# Time Complexity:  O(n) — three linear passes
# Space Complexity: O(n) — left and right arrays
# ============================================================

# ---- Tradeoffs ----
# This approach (two separate arrays):
#   Pro: Easy to understand — build left, build right, multiply
#   Con: O(n) extra space for the left and right arrays
#
# Space-optimized alternative:
#   Use the output array as the left pass, apply right on-the-fly with a variable
#   O(n) time, O(1) extra space (output array doesn't count per the problem)
#   Con: Slightly harder to follow — output array serves two purposes
#
# Division trick (not allowed by this problem):
#   product_all / nums[i] → O(n) time, O(1) space — but fails when zeros exist
#   The problem explicitly forbids using division


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
    ]

    for nums in test_cases:
        print(f"Input:  {nums}")
        print(f"Output: {productExceptSelf(nums)}")
        print()
