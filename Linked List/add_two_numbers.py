# ============================================================
# 2. Add Two Numbers
# Difficulty: Medium
#
# Problem:
# Two non-empty linked lists represent two non-negative integers
# stored in reverse order. Add the two numbers and return the
# sum as a linked list.
#
# Example 1:
#   Input:  l1 = [2,4,3], l2 = [5,6,4]
#   Output: [7,0,8]
#   Explanation: 342 + 465 = 807
#
# Example 2:
#   Input:  l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#   Output: [8,9,9,9,0,0,0,1]
# ============================================================

# ---- Strategy: Dummy Node + Carry ----
# Simulate addition digit by digit, exactly like addition on paper.
# Each step: add both digits + carry → store ones digit → carry tens digit.
#
# digit = total % 10   → last digit (what goes in new node)
# carry = total // 10  → carry to next step
#
# Use v1/v2 instead of l1.val/l2.val directly — one list might be
# shorter, so either could be None. Safe read: val if node else 0.
# Loop while l1 OR l2 OR carry — carry alone can create a final node.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0     # safe read — l1 might be None
        v2 = l2.val if l2 else 0     # safe read — l2 might be None

        total = v1 + v2 + carry
        digit = total % 10            # ones digit → store in new node
        carry = total // 10           # tens digit → carry to next step

        curr.next = ListNode(digit)   # attach new node
        curr = curr.next              # move curr forward

        l1 = l1.next if l1 else None  # move l1 forward safely
        l2 = l2.next if l2 else None  # move l2 forward safely

    return dummy.next


# ============================================================
# Dry Run: l1 = [2,4,3], l2 = [5,6,4]
# (represents 342 + 465 = 807)
# carry=0
#
# Step 1: v1=2, v2=5, total=7,  digit=7, carry=0 → node(7)
#         l1=4, l2=6
#
# Step 2: v1=4, v2=6, total=10, digit=0, carry=1 → node(0)
#         l1=3, l2=4
#
# Step 3: v1=3, v2=4, total=8,  digit=8, carry=0 → node(8)
#         l1=None, l2=None
#
# l1=None, l2=None, carry=0 → loop ends
# return 7 → 0 → 8 ✓
#
# Dry Run: l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]
#
# Step 1: 9+9=18, digit=8, carry=1 → node(8)
# Step 2: 9+9+1=19, digit=9, carry=1 → node(9)
# Step 3: 9+9+1=19, digit=9, carry=1 → node(9)
# Step 4: 9+9+1=19, digit=9, carry=1 → node(9)
# Step 5: v1=9, v2=0, 9+0+1=10, digit=0, carry=1 → node(0)
# Step 6: v1=9, v2=0, 9+0+1=10, digit=0, carry=1 → node(0)
# Step 7: v1=9, v2=0, 9+0+1=10, digit=0, carry=1 → node(0)
# Step 8: l1=None, l2=None, carry=1 → 0+0+1=1, digit=1 → node(1)
# return 8→9→9→9→0→0→0→1 ✓
#
# Time Complexity:  O(max(m,n)) — loop runs for the longer list + carry
# Space Complexity: O(max(m,n)) — new linked list of same length
# ============================================================

# ---- Tradeoffs ----
# This approach (digit by digit with carry):
#   Pro: O(max(m,n)) time — optimal, single pass
#   Pro: Handles different length lists and final carry cleanly
#
# Convert to int alternative:
#   Traverse both lists → build integers → add → convert back to list
#   Simpler to understand but fails for very large numbers (overflow)
#   Linked list approach works for numbers of any size
#
# Why while l1 or l2 or carry (not just l1 or l2):
#   Final carry can create an extra node even when both lists are done
#   Example: 9+9=18 → need extra node for the leading 1

# ---- Where I Needed Assistance ----
# 1. How carry works — thought carry goes back to previous node
#    Fix: carry goes FORWARD to the next addition, not backward
#         total % 10 = current digit, total // 10 = next carry
#
# 2. Safe value reading — wrote l1.val directly, crashes if None
#    Fix: v1 = l1.val if l1 else 0
#         always use safe read when lists can be different lengths
#
# 3. Moving l1/l2 forward — wrote l1 = l1.next, crashes if None
#    Fix: l1 = l1.next if l1 else None
#
# 4. Why loop condition includes carry
#    Fix: after both lists end, carry might still be 1
#         need one more iteration to create the final node

# ---- What to Improve ----
# - % 10 gives last digit, // 10 gives carry — memorise this
# - Always use safe reads when nodes can be None: val if node else 0
# - while l1 or l2 or carry — the carry condition is easy to forget
# - dummy node + curr pattern is the same as merge two lists


if __name__ == "__main__":
    def build_list(vals):
        if not vals:
            return None
        head = ListNode(vals[0])
        curr = head
        for v in vals[1:]:
            curr.next = ListNode(v)
            curr = curr.next
        return head

    def to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]

    for l1, l2, expected in test_cases:
        output = to_list(addTwoNumbers(build_list(l1), build_list(l2)))
        print(f"Input:    l1={l1}, l2={l2}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
