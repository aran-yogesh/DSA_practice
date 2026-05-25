# ============================================================
# 424. Longest Repeating Character Replacement
# Difficulty: Medium
#
# Problem:
# Given a string s and integer k, you can replace any character
# at most k times. Return the length of the longest substring
# containing the same letter after at most k replacements.
#
# Example 1:
#   Input:  s = "ABAB", k = 2     Output: 4
#   Explanation: Replace 'A's with 'B's → "BBBB"
#
# Example 2:
#   Input:  s = "AABABBA", k = 1  Output: 4
#   Explanation: Replace middle 'A' → "AABBBBA", longest = 4
# ============================================================

# ---- Strategy: Variable Sliding Window + Frequency Count ----
# Key insight: you never actually replace anything.
# Just check — in this window, if I keep the most frequent character
# and replace everything else, does it cost <= k replacements?
#
# replacements needed = window size - max_freq
# If replacements needed > k → window invalid → shrink from left
#
# Use a dict to count frequency of each char in the window.
# max_freq tracks the highest frequency seen — tells us the
# dominant character we would keep.


def characterReplacement(s: str, k: int) -> int:
    count = {}
    l = 0
    best = 0
    max_freq = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1       # add new char to window
        max_freq = max(max_freq, count[s[r]])        # update most frequent count

        while (r - l + 1) - max_freq > k:           # replacements needed > k
            count[s[l]] -= 1                         # remove left char from window
            l += 1                                   # shrink window

        best = max(best, r - l + 1)                 # update best valid window size

    return best


# ============================================================
# Dry Run: s = "ABAB", k = 2
# count={}, l=0, best=0, max_freq=0
#
# r=0 'A': count={'A':1}, max_freq=1
#   window=1, replacements=1-1=0 <= 2 ✓ → best=1
#
# r=1 'B': count={'A':1,'B':1}, max_freq=1
#   window=2, replacements=2-1=1 <= 2 ✓ → best=2
#
# r=2 'A': count={'A':2,'B':1}, max_freq=2
#   window=3, replacements=3-2=1 <= 2 ✓ → best=3
#
# r=3 'B': count={'A':2,'B':2}, max_freq=2
#   window=4, replacements=4-2=2 <= 2 ✓ → best=4
#
# return 4 ✓
#
# Dry Run: s = "AABABBA", k = 1
#
# r=0 'A': count={'A':1}, max_freq=1, window=1, 0<=1 ✓ best=1
# r=1 'A': count={'A':2}, max_freq=2, window=2, 0<=1 ✓ best=2
# r=2 'B': count={'A':2,'B':1}, max_freq=2, window=3, 1<=1 ✓ best=3
# r=3 'A': count={'A':3,'B':1}, max_freq=3, window=4, 1<=1 ✓ best=4
# r=4 'B': count={'A':3,'B':2}, max_freq=3, window=5, 2>1 ✗
#   → remove s[0]='A', count={'A':2,'B':2}, l=1, window=4, 2>1 ✗
#   → remove s[1]='A', count={'A':1,'B':2}, l=2, window=3, 1<=1 ✓ best=4
# r=5 'B': count={'A':1,'B':3}, max_freq=3, window=4, 1<=1 ✓ best=4
# r=6 'A': count={'A':2,'B':3}, max_freq=3, window=5, 2>1 ✗
#   → remove s[2]='B', count={'A':2,'B':2}, l=3, window=4, 2>1 ✗
#   → remove s[3]='A', count={'A':1,'B':2}, l=4, window=3, 1<=1 ✓ best=4
#
# return 4 ✓
#
# Time Complexity:  O(n) — r visits each element once
# Space Complexity: O(1) — dict has at most 26 keys (uppercase letters only)
# ============================================================

# ---- Tradeoffs ----
# This approach (sliding window):
#   Pro: O(n) time, O(1) space — optimal
#   Single pass, no actual replacements needed
#
# Brute force (check every substring):
#   O(n²) or O(n³) time — too slow for large inputs
#
# Why max_freq doesn't shrink when window shrinks:
#   When l moves right, max_freq might be stale (too high)
#   But that's okay — a stale max_freq only prevents the window
#   from growing, never causes a wrong answer
#   We only update best when window is valid, so correctness holds

# ---- Where I Needed Assistance ----
# 1. count.get(s[r], 0) — unfamiliar with .get() syntax
#    Fix: dict.get(key, default) returns default if key not found
#         same as: if key in dict: return dict[key] else: return default
#
# 2. Core insight — thought we needed to actually replace characters
#    Fix: never replace anything. Just check if replacements needed <= k
#         replacements needed = window size - most frequent char count
#
# 3. Understanding the while condition:
#    (r - l + 1) - max_freq > k
#    = window size - most frequent count > k
#    = replacements needed > k → window invalid → shrink

# ---- What to Improve ----
# - "You never actually replace" — this is the key insight to remember
# - Formula to memorise: replacements needed = window size - max_freq
# - dict.get(key, 0) + 1 is the standard way to count in a dict
# - max_freq only grows — even when stale it keeps the solution correct


if __name__ == "__main__":
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 0, 4),
        ("ABCD", 0, 1),
        ("ABCD", 4, 4),
    ]

    for s, k, expected in test_cases:
        output = characterReplacement(s, k)
        print(f"Input:    s={s!r}, k={k}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
