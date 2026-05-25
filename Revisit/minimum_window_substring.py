# ============================================================
# 76. Minimum Window Substring
# Difficulty: Hard
# Status: REVISIT — solution correct but need more practice
#         understanding have/need pattern and shrink logic
#
# Problem:
# Given strings s and t, return the minimum window substring
# of s that contains every character in t (including duplicates).
# Return "" if no such window exists.
#
# Example 1:
#   Input:  s = "ADOBECODEBANC", t = "ABC"   Output: "BANC"
# Example 2:
#   Input:  s = "a", t = "a"                 Output: "a"
# Example 3:
#   Input:  s = "a", t = "aa"                Output: ""
# ============================================================

# ---- Strategy: Variable Sliding Window + have/need pattern ----
# Two frequency dicts: t_count (fixed) and window_count (sliding).
# need = number of unique chars in t that must be satisfied.
# have = number currently satisfied in the window.
# A char c is satisfied when window_count[c] >= t_count[c].
#
# Expand r until have == need (valid window found).
# Then shrink l to minimize — stop when window becomes invalid.
# Track smallest valid window seen in result.


def minWindow(s: str, t: str) -> str:
    t_count = {}
    window_count = {}

    for c in t:
        t_count[c] = t_count.get(c, 0) + 1

    need = len(t_count)   # unique chars in t to satisfy
    have = 0              # unique chars currently satisfied
    l = 0
    result = ""

    for r in range(len(s)):
        window_count[s[r]] = window_count.get(s[r], 0) + 1

        # check if s[r] just became satisfied
        if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
            have += 1

        while have == need:                          # valid window — try to shrink
            if result == "" or (r - l + 1) < len(result):
                result = s[l:r + 1]                 # update smallest window

            window_count[s[l]] -= 1                 # remove left char
            if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                have -= 1                           # char no longer satisfied
            l += 1                                  # shrink from left

    return result


# ============================================================
# Dry Run: s = "ADOBECODEBANC", t = "ABC"
# t_count = {'A':1, 'B':1, 'C':1}, need=3
#
# r=0 'A': window={'A':1}, have=1
# r=1 'D': window={'A':1,'D':1}, have=1
# r=2 'O': have=1
# r=3 'B': window={...,'B':1}, have=2
# r=4 'E': have=2
# r=5 'C': window={...,'C':1}, have=3 → valid!
#   result="ADOBEC", remove 'A' → have=2, l=1 → exit while
# r=6 'O': have=2
# r=7 'D': have=2
# r=8 'E': have=2
# r=9 'B': window_count['B']=2, already satisfied, have stays 2
# r=10 'A': have=3 → valid!
#   window="DOBECODEBA" → longer than "ADOBEC", no update
#   remove 'D' → l=2, still valid
#   remove 'O' → l=3, still valid
#   remove 'B' → window_count['B']=1 still>=1, still valid
#   remove 'E' → l=5, still valid
#   remove 'C' → have=2, l=6 → exit while
# r=11 'N': have=2
# r=12 'C': have=3 → valid!
#   window="BANC" → shorter → result="BANC"
#   remove 'B' → have=2, l=10 → exit while
#
# return "BANC" ✓
#
# Time Complexity:  O(m + n) — m=len(s), n=len(t)
# Space Complexity: O(1)     — dicts have at most 52 keys (upper+lower)
# ============================================================

# ---- Tradeoffs ----
# This approach (variable window + have/need):
#   Pro: O(m+n) time, O(1) space — optimal
#   have/need avoids comparing full dicts every step — smarter than ==
#
# Dict comparison approach (like permutation in string):
#   Compare window_count == t_count each step → O(52) per step
#   Works but slightly less efficient; have/need is the cleaner pattern
#
# Brute force (check every substring):
#   O(m² * n) time — way too slow

# ---- Where I Needed Assistance ----
# 1. have/need pattern — didn't know how to track when window is valid
#    Fix: need = unique chars in t. have = how many are satisfied.
#         satisfied means window_count[c] >= t_count[c]
#
# 2. When to increment have:
#    Fix: only when window_count[s[r]] == t_count[s[r]] exactly
#         (not > because that means it was already satisfied)
#
# 3. Shrink logic — when to decrement have:
#    Fix: when removing s[l] causes window_count[s[l]] < t_count[s[l]]
#         that char is no longer satisfied → have -= 1
#
# 4. while have == need inside the for loop:
#    Fix: keep shrinking as long as window is valid to minimize result

# ---- What to Improve ----
# - have/need is a powerful pattern for "window contains all of t" problems
# - Expand until valid, then shrink to minimize — classic hard sliding window
# - Come back after more medium sliding window practice


if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
    ]

    for s, t, expected in test_cases:
        output = minWindow(s, t)
        print(f"Input:    s={s!r}, t={t!r}")
        print(f"Output:   {output!r}")
        print(f"Expected: {expected!r}")
        print(f"Pass:     {output == expected}")
        print()
