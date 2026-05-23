# ============================================================
# 13. Roman to Integer
# Difficulty: Easy
#
# Problem:
# Given a roman numeral string s, convert it to an integer.
# Roman numerals are usually written largest to smallest left
# to right. When a smaller value appears before a larger one,
# subtract it instead of adding.
#
# Subtraction cases:
#   IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
#
# Example 1:
#   Input:  s = "III"      Output: 3
# Example 2:
#   Input:  s = "LVIII"    Output: 58
# Example 3:
#   Input:  s = "MCMXCIV"  Output: 1994
# ============================================================

# ---- Strategy: Hashmap + one pass ----
# Store each symbol's value in a dictionary.
# Loop through the string:
#   - If current value < next value → subtract (subtraction case like IV)
#   - Otherwise → add
# Safety check: always verify next index exists before looking ahead.


def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(s)):
        # check next char exists AND current value is less than next
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]   # subtraction case e.g. I before V
        else:
            result += roman[s[i]]   # normal addition

    return result


# ============================================================
# Dry Run: s = "MCMXCIV" → expected 1994
#
# roman = {I:1, V:5, X:10, L:50, C:100, D:500, M:1000}
# result = 0
#
# i=0 'M'(1000) vs 'C'(100) → 1000 > 100 → add    → result=1000
# i=1 'C'(100)  vs 'M'(1000)→ 100  < 1000 → subtract→ result=900
# i=2 'M'(1000) vs 'X'(10)  → 1000 > 10  → add    → result=1900
# i=3 'X'(10)   vs 'C'(100) → 10   < 100 → subtract→ result=1890
# i=4 'C'(100)  vs 'I'(1)   → 100  > 1   → add    → result=1990
# i=5 'I'(1)    vs 'V'(5)   → 1    < 5   → subtract→ result=1989
# i=6 'V'(5)    no next char → add        → result=1994 ✓
#
# Time Complexity:  O(n) — single pass through string
# Space Complexity: O(1) — dictionary has fixed 7 keys
# ============================================================

# ---- Self Reflection: Where I got stuck ----
# 1. Subtraction logic — didn't know when to subtract vs add.
#    Fix: if current value < next value → subtract. That's it.
#    No need to hardcode IV, IX etc — the rule handles all cases.
#
# 2. Understanding i + 1 < len(s):
#    Fix: safety guard so we don't crash on the last character.
#    At the last index there is no s[i+1], so check first.
#    If i is the last character, this is False → just add normally.
#
# 3. Dictionary lookup roman[s[i]]:
#    s[i] is the character e.g. 'I', roman['I'] gives the value 1.
#    roman[s[i+1]] gives the NEXT character's value.
#
# ---- What to improve ----
# - When looping with index comparisons, always guard against
#   out of bounds with i + 1 < len(s) before accessing s[i+1].
# - Subtraction pattern: current < next → subtract is a common
#   trick in string problems. Remember it!
# - Dictionary with fixed known keys = O(1) space.


if __name__ == "__main__":
    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
    ]

    for s, expected in test_cases:
        output = romanToInt(s)
        print(f"Input:    {s!r}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
