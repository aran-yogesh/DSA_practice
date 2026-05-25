# ============================================================
# 567. Permutation in String
# Difficulty: Medium
#
# Problem:
# Given two strings s1 and s2, return true if s2 contains a
# permutation of s1, or false otherwise.
#
# Example 1:
#   Input:  s1 = "ab", s2 = "eidbaooo"   Output: True
#   Explanation: s2 contains "ba" which is a permutation of "ab"
#
# Example 2:
#   Input:  s1 = "ab", s2 = "eidboaoo"   Output: False
# ============================================================

# ---- Strategy: Fixed Size Sliding Window + Frequency Count ----
# Two strings are permutations of each other if they have the
# same character frequencies. No need to generate permutations.
#
# Window size = len(s1) — fixed, never changes.
# Slide window through s2, compare frequency dict with s1's dict.
# Add new right char each step, remove old left char when window too big.
# Clean up zero counts so dict comparison works correctly.


def checkInclusion(s1: str, s2: str) -> bool:
    s1_count = {}
    window_count = {}

    for c in s1:
        s1_count[c] = s1_count.get(c, 0) + 1

    for i in range(len(s2)):
        window_count[s2[i]] = window_count.get(s2[i], 0) + 1   # add right char

        if i >= len(s1):                                         # window too big
            left = s2[i - len(s1)]
            window_count[left] -= 1
            if window_count[left] == 0:
                del window_count[left]                           # clean up zeros

        if s1_count == window_count:                             # permutation found
            return True

    return False


# ============================================================
# Dry Run: s1 = "ab", s2 = "eidbaooo"
# s1_count = {'a':1, 'b':1}
#
# i=0 'e': window={'e':1},          i<2 no remove. {'e':1}!={'a':1,'b':1}
# i=1 'i': window={'e':1,'i':1},    i<2 no remove. no match
# i=2 'd': window={'e':1,'i':1,'d':1}, i>=2 remove s2[0]='e'
#          window={'i':1,'d':1}     no match
# i=3 'b': window={'i':1,'d':1,'b':1}, remove s2[1]='i'
#          window={'d':1,'b':1}     no match
# i=4 'a': window={'d':1,'b':1,'a':1}, remove s2[2]='d'
#          window={'b':1,'a':1}     == {'a':1,'b':1} → return True ✓
#
# Time Complexity:  O(n) — n = len(s2), single pass
# Space Complexity: O(1) — both dicts have at most 26 keys
# ============================================================

# ---- Tradeoffs ----
# This approach (fixed window + two frequency dicts):
#   Pro: O(n) time, O(1) space — optimal
#   Dict comparison s1_count == window_count runs O(26) per step — still O(1)
#
# Alternative — counter with match count:
#   Track how many characters have matching frequencies using a matches variable
#   Avoids full dict comparison each step — slightly faster in practice
#   Con: more complex code; dict approach is cleaner and readable
#
# Brute force (generate all permutations of s1):
#   Exponential time — never use this

# ---- Where I Needed Assistance ----
# 1. window_count[i] instead of window_count[s2[i]] — did this twice
#    Fix: key must always be the CHARACTER not the index
#         s2[i] is the character, i is just its position
#
# 2. del window_count[left] when count hits 0
#    Fix: if count drops to 0, remove the key entirely
#         otherwise {'e':0} != {} and comparison breaks

# ---- What to Improve ----
# - Dict key = character not index — burn this in, it comes up every problem
# - Fixed window: remove s2[i - len(s1)] when i >= len(s1)
# - Always clean up zero counts before comparing dicts
# - Two strings are permutations ↔ same frequency counts (no need to generate)


if __name__ == "__main__":
    test_cases = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
        ("a", "a", True),
        ("ab", "a", False),
    ]

    for s1, s2, expected in test_cases:
        output = checkInclusion(s1, s2)
        print(f"Input:    s1={s1!r}, s2={s2!r}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
