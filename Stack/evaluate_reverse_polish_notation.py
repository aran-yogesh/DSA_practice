# ============================================================
# 150. Evaluate Reverse Polish Notation
# Difficulty: Medium
#
# Problem:
# Given an array of strings tokens representing an arithmetic
# expression in Reverse Polish Notation, evaluate and return
# the result. Division truncates toward zero.
#
# Example 1:
#   Input:  tokens = ["2","1","+","3","*"]
#   Output: 9   → ((2 + 1) * 3) = 9
#
# Example 2:
#   Input:  tokens = ["4","13","5","/","+"]
#   Output: 6   → (4 + (13 / 5)) = 6
#
# Example 3:
#   Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#   Output: 22
# ============================================================

# ---- Strategy: Stack ----
# Loop through tokens:
#   - If number → push to stack
#   - If operator → pop two numbers (b first, a second),
#     apply operation, push result back
# At the end, stack has exactly one element — the answer.
#
# Key: b is popped first (top of stack), a is second.
# So operations are: a+b, a-b, a*b, int(a/b)


def evalRPN(tokens):
    result = []

    for i in tokens:
        if i == "+":
            b = result.pop()
            a = result.pop()
            result.append(a + b)
        elif i == "-":
            b = result.pop()
            a = result.pop()
            result.append(a - b)
        elif i == "/":
            b = result.pop()
            a = result.pop()
            result.append(int(a / b))   # truncate toward zero
        elif i == "*":
            b = result.pop()
            a = result.pop()
            result.append(a * b)
        else:
            result.append(int(i))       # convert string to int and push

    return result[0]   # only one element left — the final answer


# ============================================================
# Dry Run: tokens = ["2","1","+","3","*"]
#
# i="2" → number → result=[2]
# i="1" → number → result=[2,1]
# i="+" → pop b=1, pop a=2 → 2+1=3 → result=[3]
# i="3" → number → result=[3,3]
# i="*" → pop b=3, pop a=3 → 3*3=9 → result=[9]
# return result[0] = 9 ✓
#
# Dry Run: tokens = ["4","13","5","/","+"]
#
# i="4"  → number → result=[4]
# i="13" → number → result=[4,13]
# i="5"  → number → result=[4,13,5]
# i="/"  → pop b=5, pop a=13 → int(13/5)=2 → result=[4,2]
# i="+"  → pop b=2, pop a=4  → 4+2=6 → result=[6]
# return result[0] = 6 ✓
#
# Time Complexity:  O(n) — single pass through tokens
# Space Complexity: O(n) — stack stores up to n numbers
# ============================================================

# ---- Self Reflection: Where I got stuck ----
# 1. Checking if token is a number — forgot the pattern.
#    Fix: use else after all operator checks, or check i not in "+-/*"
#
# 2. Variable naming — used token instead of tokens, i inconsistently.
#    Fix: loop variable is i (current token), tokens is the full list.
#
# 3. Order of a and b — b is popped first (top of stack), a is second.
#    Fix: always pop b first, then a. Operations are a OP b not b OP a.
#    This matters for subtraction and division!
#
# 4. Division truncation — used / instead of int(a/b).
#    Fix: Python / returns float, wrap with int() to truncate toward zero.
#
# 5. Return value — returned whole list instead of result[0].
#    Fix: at the end only one element remains, return result[0] or result[-1].
#
# ---- What to improve ----
# - Understood the full algorithm before coding — great progress!
# - Mistakes were syntax/detail issues, not logic issues.
# - Always think about the ORDER when popping two elements from stack.
#   Ask: which was pushed first? which operation needs which order?
# - For division, always check: does Python's behavior match the problem?


if __name__ == "__main__":
    test_cases = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]

    expected = [9, 6, 22]

    for tokens, exp in zip(test_cases, expected):
        output = evalRPN(tokens)
        print(f"Input:    {tokens}")
        print(f"Output:   {output}")
        print(f"Expected: {exp}")
        print(f"Pass:     {output == exp}")
        print()
