# ============================================================
# 347. Top K Frequent Elements
# Difficulty: Medium
#
# Problem:
# Given an integer array nums and an integer k, return the
# k most frequent elements in any order.
#
# Example 1:
#   Input:  nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
#
# Example 2:
#   Input:  nums = [1], k = 1
#   Output: [1]
# ============================================================

# ---- Strategy: Hashmap + sort by frequency ----
# Count each number's frequency with a hashmap.
# Sort the keys by their frequency and return the top k.


def topKFrequent(nums, k):
    freq_map = {}

    for n in nums:
        if n in freq_map:
            freq_map[n] += 1
        else:
            freq_map[n] = 1

    # sort keys by frequency (highest last), return last k
    sorted_keys = sorted(freq_map, key=lambda x: freq_map[x])
    return sorted_keys[-k:]


# ============================================================
# Dry Run: nums = [1,1,1,2,2,3], k = 2
#
# freq_map = {1: 3, 2: 2, 3: 1}
# sorted by frequency → [3, 2, 1]  (lowest to highest)
# last k=2 elements  → [2, 1] ✓
#
# Time Complexity:  O(n log n) — sorting the keys
# Space Complexity: O(n) — hashmap
# ============================================================


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2),
    ]

    for nums, k in test_cases:
        print(f"Input:  nums={nums}, k={k}")
        print(f"Output: {topKFrequent(nums, k)}")
        print()
