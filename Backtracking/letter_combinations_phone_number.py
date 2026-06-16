# ============================================================
# 17. Letter Combinations of a Phone Number
# Difficulty: Medium
#
# Problem:
# Given a string containing digits from 2-9 inclusive, return
# all possible letter combinations that the number could
# represent (like an old phone keypad). Return in any order.
#
# Example 1:
#   Input:  digits = "23"   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#   Input:  digits = "2"    Output: ["a","b","c"]
# ============================================================

# ---- Strategy: Iterative Build-Up (Cartesian Product) ----
# Start with result = [""].
# For each digit, build a NEW result list by combining every
# existing string with every letter mapped to that digit.
#
# This is the same idea as a cartesian product across groups —
# combine choices from group 1 with choices from group 2, etc.
#
# Classic version of this problem uses backtracking/recursion,
# but this builds the same combinations iteratively, digit by
# digit, expanding the result list each time.

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Return every letter combination the digit string could represent."""
        if not digits:
            return []

        digit_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz",
        }

        result = [""]
        for d in digits:
            letters = digit_map[d]
            result = [combo + letter for combo in result for letter in letters]

        return result


# ============================================================
# Dry Run: digits = "23"
#
# result = [""]
#
# d='2', letters="abc"
#   result = ["" + "a", "" + "b", "" + "c"]
#          = ["a", "b", "c"]
#
# d='3', letters="def"
#   combine each of ["a","b","c"] with each of "def"
#   result = ["a"+"d","a"+"e","a"+"f",
#              "b"+"d","b"+"e","b"+"f",
#              "c"+"d","c"+"e","c"+"f"]
#          = ["ad","ae","af","bd","be","bf","cd","ce","cf"] ✓
#
# ---
# Dry Run: digits = "2"
# result = [""]
# d='2', letters="abc"
#   result = ["a","b","c"] ✓
#
# ---
# Dry Run: digits = ""
# returns [] immediately ✓
#
# Time Complexity:  O(4^n · n) — up to 4 letters per digit (digit 7/9),
#                    n digits, building strings of length n each
# Space Complexity: O(4^n · n) — storing all combinations
# ============================================================

# ---- Tradeoffs ----
# This approach (iterative cartesian product):
#   Pro: No recursion — easier to trace step by step
#   Pro: List comprehension keeps it short and readable
#   Con: Builds full intermediate lists at every digit step
#        (still fine — same total work as backtracking)
#
# Backtracking/DFS alternative:
#   Build one combination at a time via recursion, append when
#   length == len(digits). Same time complexity.
#   Pro: Doesn't materialize intermediate full lists — more natural
#        for problems where you need to prune/stop early
#   Con: Recursion is harder to trace without practice
#
# Why both are O(4^n) and not worse:
#   The number of combinations IS exponential — that's the answer
#   size, not wasted work. Can't do better than the output size.

# ---- Where I Needed Assistance ----
# 1. Combining letters across multiple digits — only had hashmap idea
#    Fix: build cartesian product — combine every existing combo
#         with every letter of the next digit
#
# 2. First attempt only appended the letter, not combo + letter
#    Fix: new_result.append(combo + letter) — needed both pieces
#
# 3. Wanted to avoid recursion/backtracking
#    Fix: same idea works iteratively — expand result list per digit
#         result = [combo + letter for combo in result for letter in letters]

# ---- What to Improve ----
# - Cartesian product pattern: result = [""] then expand per group
# - List comprehension with two for-clauses = combine two groups
# - This problem is exponential by nature — 4^n is optimal, not a flaw
# - Recursion/backtracking version of this is worth revisiting later


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("", []),
        ("9", ["w", "x", "y", "z"]),
    ]

    for digits, expected in test_cases:
        output = sol.letterCombinations(digits)
        print(f"Input:    {digits!r}")
        print(f"Output:   {sorted(output)}")
        print(f"Expected: {sorted(expected)}")
        print(f"Pass:     {sorted(output) == sorted(expected)}")
        print()
