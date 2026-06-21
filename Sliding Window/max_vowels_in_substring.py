# ============================================================
# 1456. Maximum Number of Vowels in a Substring of Given Length
# Difficulty: Medium
#
# Problem:
# Given a string s and integer k, return the maximum number of
# vowel letters in any substring of s with length k.
# Vowels: a, e, i, o, u
#
# Example 1:
#   Input:  s = "abciiidef", k = 3   Output: 3  ("iii")
# Example 2:
#   Input:  s = "aeiou", k = 2       Output: 2
# Example 3:
#   Input:  s = "leetcode", k = 3    Output: 2
# ============================================================

# ---- Strategy: Fixed Sliding Window ----
# Window size is always k. Slide one step at a time.
# Instead of recounting vowels in every new window (O(n·k)),
# just add the new right character and remove the old left character.
#
# Add:    if s[i] is vowel   → count += 1
# Remove: if s[i-k] is vowel → count -= 1
#
# s[i-k] is always the character that just LEFT the window.
# When window slides right by 1, left boundary moves from i-k to i-k+1.
# So s[i-k] is what falls off the left edge.

from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Return max vowel count in any substring of length k."""
        vowels = set("aeiou")
        count = 0
        best = 0

        # build first window (indices 0 to k-1)
        for i in range(k):
            if s[i] in vowels:
                count += 1
                best = count

        # slide window from index k to end
        for i in range(k, len(s)):
            if s[i] in vowels:      # new character enters from right
                count += 1
            if s[i - k] in vowels:  # old character exits from left
                count -= 1
            best = max(best, count)

        return best


# ============================================================
# Dry Run: s = "abciiidef", k = 3
# vowels = {'a','e','i','o','u'}
#
# ---- First window: range(3) → i = 0, 1, 2 ----
# i=0: s[0]='a' → vowel → count=1, best=1   window: [a b c]
# i=1: s[1]='b' → not vowel                  window: [a b c]
# i=2: s[2]='c' → not vowel                  window: [a b c]
# after first loop: count=1, best=1
#
# ---- Sliding window: range(3, 9) ----
#
# i=3: s[3]='i' vowel     → count=2
#      s[3-3]=s[0]='a' vowel → count=1      window: [b c i]
#      best = max(1,1) = 1
#
# i=4: s[4]='i' vowel     → count=2
#      s[4-3]=s[1]='b' not vowel             window: [c i i]
#      best = max(1,2) = 2
#
# i=5: s[5]='i' vowel     → count=3
#      s[5-3]=s[2]='c' not vowel             window: [i i i]
#      best = max(2,3) = 3
#
# i=6: s[6]='d' not vowel
#      s[6-3]=s[3]='i' vowel → count=2       window: [i i d]
#      best = max(3,2) = 3
#
# i=7: s[7]='e' vowel     → count=3
#      s[7-3]=s[4]='i' vowel → count=2       window: [i d e]
#      best = max(3,2) = 3
#
# i=8: s[8]='f' not vowel
#      s[8-3]=s[5]='i' vowel → count=1       window: [d e f]
#      best = max(3,1) = 3
#
# return 3 ✓
#
# ---- How s[i-k] works ----
# At i=3, k=3: window is indices [1,2,3] = "bci"
#   s[i]   = s[3] = 'i'  ← enters from right
#   s[i-k] = s[0] = 'a'  ← exits from left
#
# s[i-k] is always the character that just fell off the LEFT edge.
# You never need to track left pointer separately — i-k does it for you.
#
# Time Complexity:  O(n) — two passes, each O(n)
# Space Complexity: O(1) — only count and best, vowel set is fixed size
# ============================================================

# ---- Tradeoffs ----
# Fixed sliding window O(n):
#   Pro: add one, remove one — O(1) per slide
#   Pro: no left pointer needed — s[i-k] handles it automatically
#
# Brute force O(n·k):
#   Recount all k characters for every window — wasted repeated work
#   For k=1000 and n=100000 that's 100 million operations vs 100k
#
# Why set("aeiou") and not a list:
#   `in` on a set is O(1), `in` on a list is O(n)
#   Only 5 vowels so it doesn't matter here, but good habit

# ---- Where I Needed Assistance ----
# 1. Wanted to recount every window — O(n·k) brute force
#    Fix: slide one step — add right char, remove left char → O(n)
#
# 2. Forgot to initialise best after first window
#    Fix: update best inside first loop or set best=count after it
#
# 3. Wrote s[i] += 1 instead of count += 1
#    Fix: s[i] is the character — count is what you increment

# ---- What to Improve ----
# - Fixed window: build first window, then slide (add right, remove left)
# - s[i-k] = the character that exits the left — no need for a left pointer
# - Always initialise best from the first window, not just 0
# - set("aeiou") for O(1) vowel lookup


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
        ("a", 1, 1),
        ("zzzz", 2, 0),
    ]

    for s, k, expected in test_cases:
        output = sol.maxVowels(s, k)
        print(f"Input:    s={s!r}, k={k}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
