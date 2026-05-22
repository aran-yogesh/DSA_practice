# ============================================================
# 242. Valid Anagram
# Difficulty: Easy
#
# Problem:
# Given two strings s and t, return true if t is an anagram
# of s, and false otherwise.
#
# Example 1:
#   Input:  s = "anagram", t = "nagaram"
#   Output: True
#
# Example 2:
#   Input:  s = "rat", t = "car"
#   Output: False
# ============================================================

# ---- Strategy: Character frequency count with hashmaps ----
# Count each letter in s and t separately.
# If both dictionaries are equal, they are anagrams.


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for c in s:
        s_map[c] = s_map.get(c, 0) + 1

    for c in t:
        t_map[c] = t_map.get(c, 0) + 1

    return s_map == t_map


# ============================================================
# Dry Run: s = "anagram", t = "nagaram"
#
# s_map = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
# t_map = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
# s_map == t_map → True ✓
#
# Time Complexity:  O(n) — two passes through the strings
# Space Complexity: O(1) — at most 26 keys (lowercase letters)
# ============================================================


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("a", "a"),
    ]

    for s, t in test_cases:
        print(f"Input:  s={s!r}, t={t!r}")
        print(f"Output: {isAnagram(s, t)}")
        print()
