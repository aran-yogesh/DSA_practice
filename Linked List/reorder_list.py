# ============================================================
# 143. Reorder List
# Difficulty: Medium
#
# Problem:
# Given head of a linked list L0 → L1 → … → Ln
# Reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
# Do not modify node values — only change the nodes themselves.
#
# Example 1:
#   Input:  head = [1,2,3,4]     Output: [1,4,2,3]
# Example 2:
#   Input:  head = [1,2,3,4,5]   Output: [1,5,2,4,3]
# ============================================================

# ---- Strategy: 3 Steps ----
# Step 1 — Find middle using fast/slow pointers
# Step 2 — Reverse the second half
# Step 3 — Merge first and second halves alternating
#
# Key insight: you can't use len() on a linked list.
# Fast/slow finds the middle without counting.
# Cut at middle (slow.next = None) before reversing
# so the reverse doesn't bleed into the first half.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    # ---- Step 1: Find middle ----
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
    # slow is now at middle

    # ---- Step 2: Reverse second half ----
    second = slow.next    # start of second half
    slow.next = None      # cut — first half ends here

    prev = None
    curr = second

    while curr:
        next = curr.next    # save
        curr.next = prev    # reverse arrow
        prev = curr         # move prev
        curr = next         # move curr

    second = prev           # prev is new head of reversed second half

    # ---- Step 3: Merge two halves ----
    first = head            # first half starts at head

    while first and second:
        tmp1 = first.next    # save next of first
        tmp2 = second.next   # save next of second

        first.next = second  # 1 → 5
        second.next = tmp1   # 5 → 2

        first = tmp1         # move first forward
        second = tmp2        # move second forward


# ============================================================
# Dry Run: head = [1,2,3,4,5]
#
# Step 1 — Find middle:
# slow=1, fast=1
# step1: slow=2, fast=3
# step2: slow=3, fast=5 → fast.next=None → loop ends
# slow=3 (middle)
# second = 4, slow.next = None
# first half:  1 → 2 → 3 → None
# second half: 4 → 5 → None
#
# Step 2 — Reverse second half:
# prev=None, curr=4
# loop1: next=5, 4.next=None, prev=4, curr=5
# loop2: next=None, 5.next=4, prev=5, curr=None
# second = 5 → 4 → None
#
# Step 3 — Merge:
# first=1, second=5
# iter1: tmp1=2, tmp2=4
#        1.next=5, 5.next=2
#        first=2, second=4
#        list: 1→5→2→3
#
# iter2: tmp1=3, tmp2=None
#        2.next=4, 4.next=3
#        first=3, second=None
#        list: 1→5→2→4→3
#
# second=None → loop ends
# result: 1→5→2→4→3 ✓
#
# Time Complexity:  O(n) — three linear passes
# Space Complexity: O(1) — only pointers, no extra data structure
# ============================================================

# ---- Tradeoffs ----
# This approach (3 steps: find middle, reverse, merge):
#   Pro: O(n) time, O(1) space — optimal
#   Pro: Uses patterns you already know — fast/slow, reverse, merge
#
# Array conversion alternative:
#   Copy all nodes to array → reorder by index → rebuild list
#   O(n) time, O(n) space — simpler to understand but wastes memory
#   Con: len() doesn't work on linked list — need extra traversal
#
# Why you can't use len() on linked list:
#   Arrays have len() because size is stored. Linked lists don't —
#   you must traverse to count. Fast/slow avoids counting entirely.
#
# Why cut before reversing (slow.next = None):
#   Without cut, reversing second half would also reverse first half
#   Cut isolates the second half so only it gets reversed

# ---- Where I Needed Assistance ----
# 1. Breaking into 3 steps — didn't see the pattern
#    Fix: first half + reversed second half merged = reordered list
#
# 2. Why slow.next = None before reversing
#    Fix: cut isolates second half — without it reverse bleeds into first
#         always save second = slow.next BEFORE setting slow.next = None
#
# 3. Merge step — didn't know how to alternate nodes
#    Fix: save tmp1 and tmp2 first, then rewire pointers, then move forward
#         same "save before overwrite" rule as reversing
#
# 4. No return needed — function modifies in place
#    Fix: return type is None, LeetCode reads head directly

# ---- What to Improve ----
# - Fast/slow = find middle. When fast hits end, slow is at middle.
# - Always cut (slow.next = None) before reversing second half
# - Can't use len() on linked list — use fast/slow or traverse to count
# - Save tmp pointers before rewiring — same rule as reversing


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
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
    ]

    for vals, expected in test_cases:
        head = build_list(vals)
        reorderList(head)
        output = to_list(head)
        print(f"Input:    {vals}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
