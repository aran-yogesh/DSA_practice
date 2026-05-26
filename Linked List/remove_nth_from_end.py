# ============================================================
# 19. Remove Nth Node From End of List
# Difficulty: Medium
#
# Problem:
# Given the head of a linked list, remove the nth node from
# the end of the list and return its head.
#
# Example 1:
#   Input:  head = [1,2,3,4,5], n = 2   Output: [1,2,3,5]
# Example 2:
#   Input:  head = [1], n = 1            Output: []
# Example 3:
#   Input:  head = [1,2], n = 1          Output: [1]
# ============================================================

# ---- Strategy: Two Pointers (fast n+1 ahead of slow) ----
# You can't index a linked list directly — use two pointers.
# Move fast n+1 steps ahead of slow.
# When fast hits None, slow is exactly ONE node before the target.
# Then skip the target: slow.next = slow.next.next
#
# Why n+1 and not n?
#   n steps lands slow ON the target.
#   n+1 steps lands slow BEFORE the target — needed for deletion.
#
# Dummy node handles edge case when deleting the head node.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for i in range(n + 1):       # move fast n+1 steps ahead
        fast = fast.next

    while fast:                   # move both until fast hits None
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next    # skip the nth node from end

    return dummy.next             # dummy.next is real head


# ============================================================
# Dry Run: head = [1,2,3,4,5], n=2
# dummy = 0 → 1 → 2 → 3 → 4 → 5 → None
# slow=dummy(0), fast=dummy(0)
#
# Move fast n+1=3 steps:
#   i=0: fast=1
#   i=1: fast=2
#   i=2: fast=3
#   fast=3, slow=0(dummy)
#
# Move both until fast=None:
#   step1: slow=1, fast=4
#   step2: slow=2, fast=5
#   step3: slow=3, fast=None → loop ends
#
# slow=3 → one before target(4)
#   slow.next       = 4  ← delete this
#   slow.next.next  = 5  ← connect to this
#   slow.next = slow.next.next → 3.next = 5
#
# list: 0 → 1 → 2 → 3 → 5 → None
# return dummy.next = 1 → 2 → 3 → 5 ✓
#
# Dry Run: head = [1,2], n=1
# dummy = 0 → 1 → 2 → None
# Move fast 2 steps: fast=1, fast=2
# Move both: slow=1, fast=None → stop
# slow.next = slow.next.next → 1.next = None
# return dummy.next = 1 ✓
#
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — only two pointers
# ============================================================

# ---- Tradeoffs ----
# This approach (two pointers, one pass):
#   Pro: O(n) time, O(1) space — optimal
#   Pro: Single pass — no need to find length first
#
# Two pass alternative:
#   Pass 1: count length → Pass 2: go to (length - n)th node
#   Same O(n) time but two passes — less elegant
#
# Why dummy node:
#   If you delete the head (n == length), slow.next = slow.next.next
#   would fail without dummy — dummy absorbs this edge case cleanly
#
# Why n+1 not n:
#   n steps lands slow ON the target — can't delete from there
#   n+1 steps lands slow BEFORE the target — can rewire slow.next

# ---- Where I Needed Assistance ----
# 1. How to access nth node — can't use index like arrays
#    Fix: use two pointers — move fast n+1 ahead, then move both together
#
# 2. Why n+1 not n
#    Fix: deletion needs the node BEFORE the target
#         n+1 gives that one extra buffer
#
# 3. Deletion logic — thought needed a new list
#    Fix: just rewire one pointer: slow.next = slow.next.next
#         skips the target node entirely, no new list needed
#
# 4. Why dummy node
#    Fix: handles deleting the head without special case code

# ---- What to Improve ----
# - Two pointers for nth from end: fast goes n+1 ahead, not n
# - Delete a node: slow.next = slow.next.next (skip it)
# - Always use dummy when head might be deleted
# - Can't use len() on linked list — two pointers replace counting


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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
    ]

    for vals, n, expected in test_cases:
        head = build_list(vals)
        output = to_list(removeNthFromEnd(head, n))
        print(f"Input:    {vals}, n={n}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
