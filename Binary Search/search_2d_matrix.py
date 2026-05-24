# ============================================================
# 74. Search a 2D Matrix
# Difficulty: Medium
#
# Problem:
# Given an m x n matrix where each row is sorted and the first
# integer of each row is greater than the last of the previous
# row, return true if target exists in matrix, false otherwise.
# Must run in O(log(m * n)) time.
#
# Example 1:
#   Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#   Output: True
#
# Example 2:
#   Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#   Output: False
# ============================================================

# ---- Strategy: Binary Search on flattened matrix ----
# Since rows follow each other in order, treat the whole matrix
# as one flat sorted array of size m*n.
# Use indices 0 to m*n-1, convert mid to (row, col) using:
#   row = mid // n
#   col = mid % n
#
# Then apply standard binary search using matrix[row][col].


def searchMatrix(matrix, target):
    m = len(matrix)       # number of rows
    n = len(matrix[0])    # number of columns
    l = 0
    r = m * n - 1

    while l <= r:
        mid = (l + r) // 2
        row = mid // n        # which row does this flat index fall in?
        col = mid % n         # which column?

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            l = mid + 1       # target in right half
        else:
            r = mid - 1       # target in left half

    return False


# ============================================================
# Dry Run: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3
# m=3, n=4, l=0, r=11
#
# Step 1: mid=5, row=5//4=1, col=5%4=1 → matrix[1][1]=11 > 3 → r=4
# Step 2: mid=2, row=2//4=0, col=2%4=2 → matrix[0][2]=5  > 3 → r=1
# Step 3: mid=0, row=0//4=0, col=0%4=0 → matrix[0][0]=1  < 3 → l=1
# Step 4: mid=1, row=1//4=0, col=1%4=1 → matrix[0][1]=3 == 3 → return True ✓
#
# Dry Run: target=13
# Step 1: mid=5  → matrix[1][1]=11 < 13 → l=6
# Step 2: mid=8  → matrix[2][0]=23 > 13 → r=7
# Step 3: mid=6  → matrix[1][2]=16 > 13 → r=5
# l=6 > r=5 → return False ✓
#
# Time Complexity:  O(log(m*n)) — binary search over m*n elements
# Space Complexity: O(1)        — only pointers used
# ============================================================

# ---- Key Insight ----
# Treat the 2D matrix as a flat 1D array!
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# is the same as [1,3,5,7,10,11,16,20,23,30,34,60]
#
# Converting flat index to 2D:
#   row = mid // n   (integer division gives the row)
#   col = mid % n    (remainder gives the column)

# ---- Tradeoffs ----
# This approach (flatten to 1D binary search):
#   O(log(m*n)) time, O(1) space — optimal for this strict matrix type
#   Pro: Treats the entire matrix as one sorted array — single binary search
#
# Two-pass alternative:
#   Binary search for the correct row, then binary search within the row
#   O(log m + log n) = O(log(m*n)) — same complexity but two passes, more code
#
# Staircase search (top-right corner):
#   Move left if too big, down if too small → O(m + n) time
#   Works on matrices where only rows are sorted (more flexible problem)
#   Slower than binary search but handles looser matrix constraints

# ---- Where I Needed Assistance ----
# 1. Approach — tried two for loops O(m*n).
#    Fix: treat matrix as flat 1D sorted array → binary search O(log(m*n))
#
# 2. What m and n are:
#    m = len(matrix)     → number of rows
#    n = len(matrix[0])  → number of columns
#
# 3. What mid represents — flat index from 0 to m*n-1, not a direct cell
#    Fix: always convert mid → row = mid//n, col = mid%n
#
# 4. Row/col conversion formula — didn't know // and % trick
#    Fix: // gives row (how many full rows fit), % gives column (remainder)
#
# ---- What to Improve ----
# - For 2D matrix binary search: always flatten to 1D mentally first
# - Memorize: row = mid // n, col = mid % n
# - The rest is identical to standard binary search
# - Always use while l <= r not l < r


if __name__ == "__main__":
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
        ([[1]], 2, False),
    ]

    for matrix, target, expected in test_cases:
        output = searchMatrix(matrix, target)
        print(f"Input:    matrix={matrix}, target={target}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
