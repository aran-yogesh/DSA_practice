# Linked List

## What is it?
A chain of nodes. Each node has a **value** and a **pointer** to the next node.

```
1 → 2 → 3 → 4 → None
```

Unlike arrays — no index access. You must **traverse** from head using `.next`.

---

## Node structure
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## .val and .next
```
head
 ↓
[1] → [2] → [3] → None

head.val            = 1      # value of first node
head.next           = [2]    # second node
head.next.next      = [3]    # third node
head.next.next.next = None   # end of list
```

`.next` is how you move between nodes — like indexing for arrays:
```
Arrays:   nums[0]   nums[1]   nums[2]
Linked:   head      head.next head.next.next
```

---

## Types

**Singly Linked List** — each node points to next only
```
1 → 2 → 3 → None
```

**Doubly Linked List** — each node points to next AND prev
```
None ← 1 ↔ 2 ↔ 3 → None
```

**Circular** — last node points back to head
```
1 → 2 → 3 → back to 1
```

---

## When to use
- Inserting/deleting in middle → O(1) vs O(n) for arrays
- Don't know size upfront
- Problems involving reversing, merging, detecting cycles

---

## How to traverse
```python
curr = head
while curr:
    print(curr.val)
    curr = curr.next
```

---

## Null pointer crash — IMPORTANT
Accessing `.next` on `None` crashes Python:

```python
curr = curr.next    # curr is now None
curr.val            # CRASH — None has no .val
```

Always check before accessing:
```python
while curr and curr.next:   # check curr exists BEFORE curr.next
```

---

## Common operations

**Insert at head:**
```python
new_node = ListNode(0)
new_node.next = head
head = new_node
# result: 0 → 1 → 2 → 3 → None
```

**Delete a node:**
```python
curr.next = curr.next.next   # skip the next node — it's gone
```

---

## Dummy node pattern
Use when head might change — avoids edge cases:
```python
dummy = ListNode(0)
dummy.next = head
# work with dummy.next instead of head
return dummy.next
```

---

## Two pointer patterns

**Fast & slow (find middle / detect cycle):**
```python
slow = head
fast = head
while fast and fast.next:
    slow = slow.next        # moves 1 step
    fast = fast.next.next   # moves 2 steps
# slow is at middle when fast hits end
```

---

## Reversing a linked list — the golden template
Same idea as swapping two numbers with a temp variable:

```python
# swapping numbers
temp = a
a = b
b = temp

# reversing linked list
next = curr.next   # save (like temp) — ALWAYS first or you lose the chain
curr.next = prev   # reverse the arrow
prev = curr        # move prev forward
curr = next        # move curr forward (restored from save)
```

**Full reverse template:**
```python
prev = None
curr = head

while curr:
    next = curr.next   # 1. save next
    curr.next = prev   # 2. reverse arrow
    prev = curr        # 3. move prev
    curr = next        # 4. move curr

return prev            # prev is new head (curr is None at end)
```

**Why prev starts at None:**
The new tail (old head) should point to Nothing — None.

**Why return prev not curr:**
When loop ends, curr is None. prev is the new head.

---

## Key rules
1. Always check `curr` before `curr.next` — avoid null pointer crash
2. Always save `next` before changing pointers — or you lose the chain
3. Draw pointers on paper before coding — linked list is all about pointer manipulation
4. `.next` = move forward, like indexing

---

## Problems solved
| # | Problem | Difficulty |
|---|---|---|
| 206 | Reverse Linked List    | Easy |
| 21  | Merge Two Sorted Lists | Easy |
| 141 | Linked List Cycle      | Easy   |
| 2   | Add Two Numbers        | Medium |
