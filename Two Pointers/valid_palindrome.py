# ============================================================
# 125. Valid Palindrome
# Difficulty: Easy
#
# Problem:
# A phrase is a palindrome if, after converting all uppercase
# letters to lowercase and removing non-alphanumeric characters,
# it reads the same forward and backward.
#
# Example 1:
#   Input:  s = "A man, a plan, a canal: Panama"
#   Output: True
#
# Example 2:
#   Input:  s = "race a car"
#   Output: False
#
# Example 3:
#   Input:  s = " "
#   Output: True
# ============================================================

# ---- Strategy: Clean string + reverse check ----
# 1. Loop through s, keep only alphanumeric chars (isalnum())
# 2. Lowercase everything
# 3. Check if cleaned string equals its reverse


def isPalindrome(s):
    clean = ""

    for c in s:
        if c.isalnum():
            clean += c.lower()

    return clean == clean[::-1]


# ============================================================
# Dry Run: s = "A man, a plan, a canal: Panama"
#
# After cleaning: "amanaplanacanalpanama"
# Reversed:       "amanaplanacanalpanama"
# Equal → True ✓
#
# Time Complexity:  O(n) — one pass to clean + one to reverse
# Space Complexity: O(n) — the cleaned string
# ============================================================

# ---- Tradeoffs ----
# This approach (build cleaned string + reverse check):
#   Pro: Very readable — clean first, then compare
#   Con: O(n) extra space for the cleaned string
#
# True two-pointer alternative (O(1) space):
#   Keep l and r on original string, skip non-alphanumeric chars inline
#   Compare lowercased chars directly — never builds a new string
#   Pro: O(1) space  Con: More code to handle skipping invalid chars
#
# For most interviews either is acceptable.
# If asked to minimize space, use the two-pointer approach on the original string.


if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]

    for s in test_cases:
        print(f"Input:  {s!r}")
        print(f"Output: {isPalindrome(s)}")
        print()
