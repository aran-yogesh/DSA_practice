# ============================================================
# 21. Merge Two Sorted Lists
# Difficulty: Easy
#
# Problem:
# Given the heads of two sorted linked lists, merge them into
# one sorted linked list and return the head.
#
# Example 1:
#   Input:  list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]
# Example 2:
#   Input:  list1 = [], list2 = []
#   Output: []
# Example 3:
#   Input:  list1 = [], list2 = [0]
#   Output: [0]
# ============================================================

# ---- Strategy: Dummy Node + Two Pointers ----
# Same idea as merging two sorted arrays — compare front of each
# list, pick the smaller one, attach it, move that pointer forward.
#
# Dummy node avoids edge cases with the head — build result from
# dummy.next so we never worry about initialising head separately.
# curr builds the merged list by moving forward each step.
# After the loop, attach whichever list still has nodes remaining.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1        # attach smaller node
            list1 = list1.next       # move list1 forward
        else:
            curr.next = list2        # attach smaller node
            list2 = list2.next       # move list2 forward
        curr = curr.next             # move curr forward

    if list1:
        curr.next = list1            # attach remaining list1
    if list2:
        curr.next = list2            # attach remaining list2

    return dummy.next                # dummy.next is the real head


# ============================================================
# Dry Run: list1 = 1→2→4, list2 = 1→3→4
# dummy=0, curr=dummy
#
# Loop 1: list1.val=1, list2.val=1 → equal → take list1
#   curr.next=1(list1), list1=2, curr=1
#   state: 0→1, curr at 1
#
# Loop 2: list1.val=2, list2.val=1 → take list2
#   curr.next=1(list2), list2=3, curr=1
#   state: 0→1→1, curr at second 1
#
# Loop 3: list1.val=2, list2.val=3 → take list1
#   curr.next=2, list1=4, curr=2
#   state: 0→1→1→2
#
# Loop 4: list1.val=4, list2.val=3 → take list2
#   curr.next=3, list2=4, curr=3
#   state: 0→1→1→2→3
#
# Loop 5: list1.val=4, list2.val=4 → equal → take list1
#   curr.next=4(list1), list1=None, curr=4
#   state: 0→1→1→2→3→4
#
# list1=None, list2=4 → attach list2
#   curr.next=4(list2)
#   state: 0→1→1→2→3→4→4
#
# return dummy.next = 1→1→2→3→4→4 ✓
#
# Time Complexity:  O(m+n) — visit each node once
# Space Complexity: O(1)   — only pointers, no new nodes created
# ============================================================

# ---- Tradeoffs ----
# This approach (dummy node + two pointers):
#   Pro: O(m+n) time, O(1) space — optimal
#   Pro: Dummy node removes head edge case cleanly
#
# Recursive alternative:
#   Cleaner to read but O(m+n) space from call stack
#   Con: Stack overflow risk on very long lists
#
# New list alternative:
#   Create new nodes for each value → O(m+n) space — wasteful

# ---- Where I Needed Assistance ----
# 1. Comparing nodes instead of values — wrote list1 <= list2
#    Fix: always compare list1.val <= list2.val not the nodes themselves
#
# 2. curr.next typo — wrote curr.nest
#    Fix: it's always curr.next — burn this in
#
# 3. curr = curr.next missing inside while loop
#    Fix: curr must move forward every iteration or you overwrite same node
#
# 4. Return dummy.next not curr
#    Fix: curr is at the end of the list. dummy.next is the real head.

# ---- What to Improve ----
# - Dummy node pattern: use whenever head might change or is unknown
#   Always return dummy.next at the end
# - Always compare .val not the nodes themselves
# - curr = curr.next goes INSIDE the loop — easy to forget
# - After while loop, attach remaining with if list1 / if list2


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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [2], [1, 2]),
    ]

    for l1, l2, expected in test_cases:
        output = to_list(mergeTwoLists(build_list(l1), build_list(l2)))
        print(f"Input:    list1={l1}, list2={l2}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
