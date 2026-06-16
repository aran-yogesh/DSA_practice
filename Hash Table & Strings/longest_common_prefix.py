# ============================================================
# 14. Longest Common Prefix
# Difficulty: Easy
#
# Problem:
# Write a function to find the longest common prefix string
# amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
#   Input:  strs = ["flower","flow","flight"]   Output: "fl"
# Example 2:
#   Input:  strs = ["dog","racecar","car"]       Output: ""
# ============================================================

# ---- Strategy: Character by Character (Vertical Scan) ----
# Pick the first string as a reference.
# For each position i, check that character against every other
# string at the same position.
# The moment any string is shorter than i OR has a different
# character at i → return what we have so far.
#
# Why strs[0] as reference?
#   The common prefix can't be longer than any single string,
#   so we iterate up to the length of the first string.
#   Any mismatch or length exceeded → we stop.
#
# Why len(word) <= i first?
#   Short-circuit: if the word is too short, don't try word[i]
#   — that would crash with an index out of bounds error.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Find the longest prefix shared by all strings in the list."""
        ans = ""

        for i in range(len(strs[0])):
            for word in strs:
                if len(word) <= i or word[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]

        return ans


# ============================================================
# Dry Run: strs = ["flower", "flow", "flight"]
# reference = strs[0] = "flower"
# ans = ""
#
# i=0 (checking 'f'):
#   word="flower": len=6>0, word[0]='f' == strs[0][0]='f' → ok
#   word="flow":   len=4>0, word[0]='f' == 'f' → ok
#   word="flight": len=6>0, word[0]='f' == 'f' → ok
#   all match → ans += 'f' → ans = "f"
#
# i=1 (checking 'l'):
#   word="flower": word[1]='l' == 'l' → ok
#   word="flow":   word[1]='l' == 'l' → ok
#   word="flight": word[1]='l' == 'l' → ok
#   all match → ans += 'l' → ans = "fl"
#
# i=2 (checking 'o'):
#   word="flower": word[2]='o' == 'o' → ok
#   word="flow":   word[2]='o' == 'o' → ok
#   word="flight": word[2]='i' != 'o' → return "fl" ✓
#
# ---
# Dry Run: strs = ["ab", "a"]
# reference = "ab", ans = ""
#
# i=0: word="ab" ok, word="a" ok → ans = "a"
# i=1: word="ab" ok, word="a": len("a")=1 <= 1 → return "a" ✓
#
# ---
# Dry Run: strs = ["dog","racecar","car"]
# reference = "dog", ans = ""
#
# i=0: word="dog" ok, word="racecar": word[0]='r' != 'd' → return "" ✓
#
# Time Complexity:  O(n·m) — n strings, m = length of shortest string
# Space Complexity: O(1) — only the answer string, no extra data structure
# ============================================================

# ---- Tradeoffs ----
# This approach (vertical scan):
#   Pro: O(n·m) — optimal, you must read every character at least once
#   Pro: Stops early the moment a mismatch is found
#   Pro: O(1) space — only building the answer string
#
# Sort trick alternative:
#   Sort strings → compare only first and last
#   O(n log n) for sort — actually worse than vertical scan
#   Not worth it here
#
# Why O(n·m) is optimal:
#   You can't find the common prefix without reading characters.
#   O(n·m) is just the size of the input — can't do better.

# ---- Where I Needed Assistance ----
# 1. Overcomplicating — thought hashtable or sliding window
#    Fix: just pick one word as reference, compare position by position
#
# 2. What to compare — was unsure what word[i] compares against
#    Fix: strs[0][i] — the same position in the reference word
#
# 3. Edge case ["ab", "a"] — crashes without length check
#    Fix: len(word) <= i check before word[i] prevents index out of bounds
#         Python short-circuits OR — if first is True, second never runs

# ---- What to Improve ----
# - Vertical scan: outer loop = positions, inner loop = all strings
# - Always check length before accessing index on variable-length strings
# - strs[0][i] = character at position i of the reference string
# - Return ans immediately on mismatch — don't wait for inner loop to finish


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["ab", "a"], "a"),
        (["a"], "a"),
        (["flower", "flower", "flower"], "flower"),
    ]

    for strs, expected in test_cases:
        output = sol.longestCommonPrefix(strs)
        print(f"Input:    {strs}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
