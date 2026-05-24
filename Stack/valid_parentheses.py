# ============================================================
# 20. Valid Parentheses
# Difficulty: Easy
#
# Problem:
# Given a string s containing just '(', ')', '{', '}', '[', ']',
# determine if the input string is valid.
# Valid means: open brackets closed in correct order and type.
#
# Example 1:
#   Input:  s = "()"       Output: True
# Example 2:
#   Input:  s = "()[]{}"   Output: True
# Example 3:
#   Input:  s = "(]"       Output: False
# Example 4:
#   Input:  s = "([])"     Output: True
# Example 5:
#   Input:  s = "([)]"     Output: False
# ============================================================

# ---- Strategy: Stack + Dictionary ----
# Push opening brackets onto the stack.
# When a closing bracket is seen, pop from stack and check
# if it matches the expected opening bracket using a dictionary.
# At the end, stack must be empty — any leftovers mean unclosed brackets.


def isValid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    st = []

    for i in s:
        if i in '([{':
            st.append(i)        # push opening bracket
        elif i in pairs:
            if not st or st.pop() != pairs[i]:  # pop and check match
                return False

    return len(st) == 0         # empty stack = all brackets matched


# ============================================================
# Dry Run: s = "([)]"
#
# i='(' → opening → push → st=['(']
# i='[' → opening → push → st=['(','[']
# i=')' → closing → pop '[' → pairs[')']='(' → '[' != '(' → return False ✓
#
# Dry Run: s = "{[]}"
#
# i='{' → opening → push → st=['{']
# i='[' → opening → push → st=['{','[']
# i=']' → closing → pop '[' → pairs[']']='[' → '[' == '[' ✓ continue
# i='}' → closing → pop '{' → pairs['}']='{{' → '{' == '{' ✓ continue
# loop ends → len(st)==0 → return True ✓
#
# Time Complexity:  O(n) — single pass through string
# Space Complexity: O(n) — stack can hold up to n characters
# ============================================================

# ---- Tradeoffs ----
# This approach (stack + dictionary):
#   O(n) time, O(n) space
#   Pro: General — handles all bracket types with one clean dictionary lookup
#
# Counter-based approach (only valid for single bracket type):
#   Track open count, increment '(', decrement ')' → O(1) space
#   Con: Breaks immediately with mixed types — cannot detect "([)]" as invalid
#
# Stack is the only correct general solution; counters are insufficient

# ---- Self Reflection: Where I got stuck ----
# 1. Pop logic — thought to pop only when bracket is "wrong".
#    Fix: always pop when you see a closing bracket, THEN check if it matches.
#
# 2. elif syntax — tried s[i].pop() instead of just checking i in pairs.
#    Fix: i is the character itself, use i in pairs to check if it's closing.
#
# 3. return True inside loop — returned too early after first match.
#    Fix: never return True inside the loop, only return False on mismatch.
#    Return True/False only after the loop is fully done.
#
# 4. End condition — didn't think about unclosed brackets like "(((".
#    Fix: after the loop, return len(st) == 0.
#    Empty stack = all matched. Non-empty = some never closed.
#
# ---- What to improve ----
# - Always ask edge case questions before coding:
#   "What if stack is empty when I try to pop?"
#   "What if the loop ends but stack still has items?"
# - Don't return True/False prematurely inside a loop.
# - Remember: pop() both reads AND removes in one step.


if __name__ == "__main__":
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([])",
        "([)]",
        "(((",
    ]

    for s in test_cases:
        print(f"Input:  {s!r}")
        print(f"Output: {isValid(s)}")
        print()
