# ============================================================
# 49. Group Anagrams
# Difficulty: Medium
#
# Problem:
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# Example 1:
#   Input:  strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
#   Input:  strs = [""]
#   Output: [[""]]
# ============================================================

# ---- Strategy: Sorted string as hashmap key ----
# Anagrams always produce the same string when sorted.
# Use the sorted word as the key, group original words as values.


def groupAnagrams(strs):
    word_map = {}

    for w in strs:
        key = "".join(sorted(w))  # "eat" → "aet", "tea" → "aet"
        if key in word_map:
            word_map[key].append(w)
        else:
            word_map[key] = [w]

    return list(word_map.values())


# ============================================================
# Dry Run: strs = ["eat","tea","tan","ate","nat","bat"]
#
# "eat" → key="aet" → {"aet": ["eat"]}
# "tea" → key="aet" → {"aet": ["eat","tea"]}
# "tan" → key="ant" → {"aet": ["eat","tea"], "ant": ["tan"]}
# "ate" → key="aet" → {"aet": ["eat","tea","ate"], ...}
# "nat" → key="ant" → {..., "ant": ["tan","nat"]}
# "bat" → key="abt" → {..., "abt": ["bat"]}
#
# Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]] ✓
#
# Time Complexity:  O(n * k log k) — n words, k = avg word length
# Space Complexity: O(n) — storing all words in the hashmap
# ============================================================

# ---- Tradeoffs ----
# This approach (sorted string as key):
#   Pro: Simple and readable — sorted("eat") == "aet" is intuitive
#   Con: O(k log k) per word for sorting — adds up for many long words
#
# Alternative — Character frequency tuple as key:
#   Count each of 26 letters → use tuple of counts as key → O(k) per word
#   Faster for long strings but slightly more code
#
# For typical inputs (short words) sorted string is fine.
# For large inputs with very long words, frequency tuple is faster.


if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
    ]

    for strs in test_cases:
        print(f"Input:  {strs}")
        print(f"Output: {groupAnagrams(strs)}")
        print()
