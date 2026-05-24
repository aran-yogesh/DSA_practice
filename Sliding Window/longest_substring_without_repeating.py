# ============================================================
# 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
#
# Problem:
# Given a string s, find the length of the longest substring
# without duplicate characters.
#
# Example 1:
#   Input:  s = "abcabcbb"   Output: 3  ("abc")
# Example 2:
#   Input:  s = "bbbbb"      Output: 1  ("b")
# Example 3:
#   Input:  s = "pwwkew"     Output: 3  ("wke")
# ============================================================

# ---- Strategy: Variable Size Sliding Window + Set ----
# Use two pointers l and r to define the current window.
# r expands right every step — adding new characters.
# When a duplicate is found, shrink from the left until clean.
# Track seen characters in a set for O(1) lookup.
# Window size at any point = r - l + 1.


def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    l = 0
    best = 0

    for r in range(len(s)):
        while s[r] in seen:       # duplicate found — shrink from left
            seen.remove(s[l])
            l += 1
        seen.add(s[r])            # add new character to window
        best = max(best, r - l + 1)  # update best window size

    return best


# ============================================================
# Dry Run: s = "abcabcbb"
#
# r=0 'a' not in seen → add → seen={'a'},         best=1 (0-0+1)
# r=1 'b' not in seen → add → seen={'a','b'},     best=2 (1-0+1)
# r=2 'c' not in seen → add → seen={'a','b','c'}, best=3 (2-0+1)
# r=3 'a' in seen → remove s[0]='a', l=1
#       'a' not in seen → add → seen={'b','c','a'},best=3 (3-1+1)
# r=4 'b' in seen → remove s[1]='b', l=2
#       'b' not in seen → add → seen={'c','a','b'},best=3 (4-2+1)
# r=5 'c' in seen → remove s[2]='c', l=3
#       'c' not in seen → add → seen={'a','b','c'},best=3 (5-3+1)
# r=6 'b' in seen → remove s[3]='a', l=4
#       'b' in seen → remove s[4]='b', l=5
#       'b' not in seen → add → seen={'c','b'},   best=3 (6-5+1)
# r=7 'b' in seen → remove s[5]='c', l=6
#       'b' in seen → remove s[6]='b', l=7
#       'b' not in seen → add → seen={'b'},       best=3 (7-7+1)
#
# return 3 ✓
#
# Time Complexity:  O(n) — each character added and removed at most once
# Space Complexity: O(min(n, 26)) — set holds at most unique chars
# ============================================================

# ---- Tradeoffs ----
# This approach (set + variable window):
#   Pro: O(n) time — each character touched at most twice (add + remove)
#   Pro: Clean and readable
#
# Brute force alternative:
#   Check every substring → O(n²) or O(n³) time — too slow
#
# Hashmap alternative:
#   Store index of each character instead of just presence
#   Allows jumping l directly to the right position instead of sliding
#   O(n) time but slightly more complex — set approach is simpler here

# ---- Self Reflection: Where I got stuck ----
# 1. Using if instead of while — one removal might not be enough
#    Fix: use while so we keep shrinking until the duplicate is fully gone
#
# 2. Not updating best — forgot to track the max window size
#    Fix: best = max(best, r - l + 1) after every valid window
#
# 3. r - l + 1 — why +1?
#    Fix: indices l to r inclusive = r - l + 1 elements
#    Example: l=0, r=2 → indices 0,1,2 → 3 elements = 2-0+1

# ---- What to Improve ----
# - Variable window pattern: r always moves, l only moves when broken
# - Always use while (not if) when shrinking — one removal may not fix it
# - Window size = r - l + 1 (always, for any window problem)
# - Set = O(1) check for "is this already in my window?"


if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("au", 2),
    ]

    for s, expected in test_cases:
        output = lengthOfLongestSubstring(s)
        print(f"Input:    {s!r}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
