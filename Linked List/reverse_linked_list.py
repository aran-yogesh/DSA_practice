# ============================================================
# 206. Reverse Linked List
# Difficulty: Easy
#
# Problem:
# Given the head of a singly linked list, reverse the list
# and return the reversed list.
#
# Example 1:
#   Input:  head = [1,2,3,4,5]   Output: [5,4,3,2,1]
# Example 2:
#   Input:  head = [1,2]         Output: [2,1]
# Example 3:
#   Input:  head = []            Output: []
# ============================================================

# ---- Strategy: Two Pointers (prev and curr) ----
# Reverse the arrows in place — no new list needed.
# prev starts at None (new tail points to nothing).
# curr starts at head.
# Each step: save next, reverse arrow, move both pointers forward.
# Same concept as swapping two numbers with a temp variable.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        next = curr.next   # save next — ALWAYS first or you lose the chain
        curr.next = prev   # reverse the arrow
        prev = curr        # move prev forward
        curr = next        # move curr forward

    return prev            # prev is the new head


# ============================================================
# Dry Run: head = 1 → 2 → 3 → None
# prev=None, curr=1
#
# Loop 1:
#   next = curr.next = 2
#   curr.next = prev → 1.next = None   (1 → None)
#   prev = 1
#   curr = 2
#
# Loop 2:
#   next = curr.next = 3
#   curr.next = prev → 2.next = 1   (2 → 1 → None)
#   prev = 2
#   curr = 3
#
# Loop 3:
#   next = curr.next = None
#   curr.next = prev → 3.next = 2   (3 → 2 → 1 → None)
#   prev = 3
#   curr = None
#
# curr=None → loop ends → return prev=3
# Result: 3 → 2 → 1 → None ✓
#
# Time Complexity:  O(n) — visit each node once
# Space Complexity: O(1) — only two pointers, no extra data structure
# ============================================================

# ---- Tradeoffs ----
# This approach (in-place reversal):
#   O(n) time, O(1) space — optimal
#   Pro: No extra memory — arrows reversed in place
#
# New list alternative:
#   Create new nodes in reverse order → O(n) time, O(n) space
#   Pro: Easier to visualise  Con: Wastes memory
#
# Recursive approach:
#   O(n) time, O(n) space (call stack)
#   Con: Space is worse than iterative — use iterative

# ---- Self Reflection: Where I got stuck ----
# 1. Why prev — didn't understand what to point curr.next backwards to
#    Fix: prev is where curr should point after reversal
#         starts at None because new tail points to nothing
#
# 2. Why save next first — almost overwrote curr.next without saving
#    Fix: once you do curr.next = prev, you lose the rest of the list
#         always save next BEFORE changing anything
#
# 3. Why return prev not curr
#    Fix: when loop ends curr is None. prev is the new head.
#
# 4. Understanding .next — confused about how to access nodes
#    Fix: .next is like indexing. head.next = second node, same as nums[1]

# ---- What to Improve ----
# - Four lines inside while — memorise the ORDER:
#   1. next = curr.next   (save)
#   2. curr.next = prev   (reverse)
#   3. prev = curr        (move prev)
#   4. curr = next        (move curr)
# - prev=None, curr=head — always this initialisation for reversal
# - Return prev — curr is None at the end, prev is new head


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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]

    for vals, expected in test_cases:
        head = build_list(vals)
        output = to_list(reverseList(head))
        print(f"Input:    {vals}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
