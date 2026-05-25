# ============================================================
# 141. Linked List Cycle
# Difficulty: Easy
#
# Problem:
# Given head of a linked list, determine if it has a cycle.
# A cycle exists if a node can be reached again by following
# next pointers. Return true if cycle exists, false otherwise.
#
# Example 1:
#   Input:  head = [3,2,0,-4], pos = 1   Output: true
#   Explanation: tail connects back to index 1 (node 2)
#
# Example 2:
#   Input:  head = [1,2], pos = 0        Output: true
#
# Example 3:
#   Input:  head = [1], pos = -1         Output: false
# ============================================================

# ============================================================
# Solution 1 — Set (O(n) space)
# ---- Strategy ----
# Store every visited node in a set.
# If you see the same node again → cycle exists.
# If you reach None → no cycle.
#
# Key: store the NODE OBJECT not the value.
# Two nodes can have the same value but not be the same node.
# ============================================================

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle_set(head: Optional[ListNode]) -> bool:
    seen = set()
    curr = head

    while curr:
        if curr in seen:      # same node seen again → cycle
            return True
        seen.add(curr)        # mark node as visited
        curr = curr.next

    return False              # reached None → no cycle


# ============================================================
# Solution 2 — Fast & Slow Pointers (O(1) space)
# ---- Strategy ----
# slow moves 1 step, fast moves 2 steps.
# If there is a cycle, fast will lap slow and they will meet.
# If no cycle, fast hits None and loop ends.
#
# Like two runners on a track — if the track is circular,
# the faster runner will always catch the slower one.
# ============================================================

def hasCycle_fast_slow(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:     # fast.next check prevents crash on next.next
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps

        if slow == fast:          # same NODE (not same value) → cycle
            return True

    return False                  # fast hit None → no cycle


# ============================================================
# Dry Run (Fast/Slow): head = [3,2,0,-4], pos=1
# Cycle: -4 connects back to node 2 (index 1)
# 3 → 2 → 0 → -4
#     ↑__________↓
#
# slow=3, fast=3
#
# Step 1:
#   slow = 2
#   fast = 0   (3→2→0, two steps)
#   2 != 0
#
# Step 2:
#   slow = 0
#   fast = 2   (0→-4→2, two steps)
#   0 != 2
#
# Step 3:
#   slow = -4
#   fast = -4  (2→0→-4, two steps)
#   slow == fast → return True ✓
#
# Dry Run (Fast/Slow): head = [1,2,3], no cycle
#
# slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=None → while fails → return False ✓
#
# ============================================================
# Time Complexity:  O(n) — both solutions visit each node once
# Space Complexity: O(n) — set solution stores all nodes
#                   O(1) — fast/slow only uses two pointers
# ============================================================

# ---- Tradeoffs ----
# Set approach:
#   Pro: Easy to understand — "have I seen this node before?"
#   Con: O(n) space — stores every node
#
# Fast/slow approach:
#   Pro: O(1) space — only two pointers
#   Con: Harder to understand initially
#   Pro: Works for ANY cycle regardless of where it connects back
#
# Key insight for both: compare NODE OBJECTS not values
#   Two nodes can have same value but be different nodes — not a cycle
#   slow == fast checks same node in memory, not same value

# ---- Where I Needed Assistance ----
# 1. Traversing forever on a cycled list — thought we could just traverse to end
#    Fix: if there's a cycle there IS no end — you loop forever
#         need a smarter approach to detect without hitting None
#
# 2. Fast/slow concept — didn't understand why they'd meet
#    Fix: think of two runners on a circular track
#         faster one always laps the slower one if track loops
#
# 3. Why fast.next check in while condition
#    Fix: fast moves two steps → fast.next.next
#         if fast.next is None, fast.next.next crashes
#         check fast.next first to prevent this
#
# 4. Comparing nodes not values
#    Fix: slow == fast compares the actual node objects
#         slow.val == fast.val would be wrong — same value ≠ same node

# ---- What to Improve ----
# - Fast/slow = go-to pattern for cycle detection and finding middle
# - Always use while fast and fast.next (not just while fast)
# - Store node objects in set, not values
# - If a list has a cycle it has no None — traversal never ends


if __name__ == "__main__":
    # Test 1: cycle at pos=1
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # cycle back to n2

    print(f"Test 1 (cycle at pos=1):")
    print(f"Set:        {hasCycle_set(n1)}")       # True
    print(f"Fast/slow:  {hasCycle_fast_slow(n1)}")  # True
    print()

    # Test 2: no cycle
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a1.next = a2
    a2.next = a3

    print(f"Test 2 (no cycle):")
    print(f"Set:        {hasCycle_set(a1)}")       # False
    print(f"Fast/slow:  {hasCycle_fast_slow(a1)}")  # False
