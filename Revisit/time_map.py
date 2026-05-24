# ============================================================
# 981. Time Based Key-Value Store
# Difficulty: Medium
# Status: REVISIT — solution coded correctly but visualisation
#         and logic building was hard; needs more practice
#
# Problem:
# Design a time-based key-value store that stores multiple values
# for the same key at different timestamps and retrieves the value
# at a certain timestamp.
#
# TimeMap() — initializes the data structure
# set(key, value, timestamp) — stores key→value at timestamp
# get(key, timestamp) — returns the value with the largest
#   timestamp_prev <= timestamp. Returns "" if none exists.
#
# Example:
#   set("foo", "bar",  1)
#   get("foo", 1)  → "bar"
#   get("foo", 3)  → "bar"   (no entry at 3, closest before = 1)
#   set("foo", "bar2", 4)
#   get("foo", 4)  → "bar2"
#   get("foo", 5)  → "bar2"  (no entry at 5, closest before = 4)
# ============================================================

# ---- Strategy: Hashmap + Binary Search ----
# set(): store (value, timestamp) pairs in a list per key.
#   Timestamps always arrive in increasing order → list is always sorted.
#
# get(): binary search the list for the largest timestamp <= given timestamp.
#   Keep updating res whenever a valid (<=) timestamp is found.
#   Move l right to try to find an even larger valid timestamp.
#   Return res at the end ("" if no valid entry was ever found).


class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]    # valid candidate — save it
                l = mid + 1             # try to find a larger valid timestamp
            else:
                r = mid - 1             # timestamp too big, go left

        return res


# ============================================================
# Dry Run: set("foo","bar",1), set("foo","bar2",4)
# dic = {"foo": [["bar",1], ["bar2",4]]}
#
# get("foo", 3):
#   values = [["bar",1], ["bar2",4]], l=0, r=1
#   mid=0 → timestamp 1 <= 3 ✓ → res="bar",  l=1
#   mid=1 → timestamp 4 <= 3 ✗ → r=0
#   l > r → return "bar" ✓
#
# get("foo", 5):
#   values = [["bar",1], ["bar2",4]], l=0, r=1
#   mid=0 → timestamp 1 <= 5 ✓ → res="bar",  l=1
#   mid=1 → timestamp 4 <= 5 ✓ → res="bar2", l=2
#   l > r → return "bar2" ✓
#
# Time Complexity:  set O(1) | get O(log n) — binary search over timestamps
# Space Complexity: O(n) — storing all (value, timestamp) pairs
# ============================================================

# ---- Tradeoffs ----
# This approach (hashmap + binary search):
#   Pro: O(log n) get — fast even with many timestamps per key
#   Con: Slightly more complex than linear scan
#
# Linear scan alternative for get():
#   Loop through list, keep updating res while timestamp <= given → O(n)
#   Simpler code but too slow when a key has many timestamps
#
# Why binary search works here:
#   Timestamps are guaranteed to arrive in increasing order → list always sorted
#   Without that guarantee, you'd have to sort first before binary searching

# ---- Where I Needed Assistance ----
# 1. Visualising the problem — hard to understand what get() is really asking
#    Fix: think of it as a notebook — find the most recent entry at or before time T
#
# 2. Binary search direction — not obvious which way to move l and r
#    Fix: if timestamp valid (<=), save res and move l RIGHT to find a bigger valid one
#         if timestamp too big, move r LEFT
#
# 3. Combining two concepts (hashmap + binary search) felt overwhelming
#    Fix: solve them separately — set() is just hashmap, get() is just binary search

# ---- What to Improve ----
# - This is hashmap + binary search combined — practice each pattern separately first
# - The "save candidate and keep searching right" pattern appears often:
#   whenever you need the LARGEST value that satisfies a condition
# - Come back after more binary search reps and this will feel natural
