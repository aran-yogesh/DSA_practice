# DSA Practice

Personal DSA problem solving practice with guided brainstorming.

## How to resume the coding session

```bash
claude --resume "coding practice"
```

## Structure

```
Arrays & Hashing/
├── contains_duplicate.py
├── valid_anagram.py
├── two_sum.py
├── group_anagrams.py
├── top_k_frequent.py
├── product_except_self.py
└── longest_consecutive_sequence.py

Two Pointers/
├── valid_palindrome.py
├── two_sum_ii.py
├── 3sum.py
├── container_with_most_water.py
└── trapping_rain_water.py

Stack/
└── valid_parentheses.py
```

Each file contains:
- Problem statement
- Strategy explanation
- Solution
- Dry run with step by step trace
- Time and space complexity
- Self reflection (what I got stuck on and what to improve)

---

## Problems Solved

### Arrays & Hashing

| Problem | Difficulty | Key Technique | Time | Space |
|---------|-----------|---------------|------|-------|
| 217. Contains Duplicate | Easy | Set comparison | O(n) | O(n) |
| 242. Valid Anagram | Easy | Character frequency hashmap | O(n) | O(1) |
| 1. Two Sum | Easy | Hashmap complement lookup | O(n) | O(n) |
| 49. Group Anagrams | Medium | Sorted string as hashmap key | O(n·k log k) | O(n) |
| 347. Top K Frequent Elements | Medium | Hashmap + sort by frequency | O(n log n) | O(n) |
| 238. Product of Array Except Self | Medium | Prefix and suffix products | O(n) | O(n) |
| 128. Longest Consecutive Sequence | Medium | Set + sequence start detection | O(n) | O(n) |

### Two Pointers

| Problem | Difficulty | Key Technique | Time | Space |
|---------|-----------|---------------|------|-------|
| 125. Valid Palindrome | Easy | Clean string + reverse check | O(n) | O(n) |
| 167. Two Sum II | Medium | Two pointers on sorted array | O(n) | O(1) |
| 15. 3Sum | Medium | Sort + fix one + two pointers | O(n²) | O(n) |
| 11. Container With Most Water | Medium | Two pointers, move shorter wall | O(n) | O(1) |
| 42. Trapping Rain Water | Hard | Two pointers with running max | O(n) | O(1) |

### Stack

| Problem | Difficulty | Key Technique | Time | Space |
|---------|-----------|---------------|------|-------|
| 20. Valid Parentheses | Easy | Stack + dictionary for pairs | O(n) | O(n) |

---

## Key Learnings by Topic

### Arrays & Hashing
- Always decide key and value before coding a hashmap
- Set gives O(1) lookup — use it when you only need existence check
- Counter and sorted string are powerful tricks for anagram problems
- Prefix/suffix arrays let you avoid recomputing products

### Two Pointers
- Use when array is sorted or you need pairs/triplets
- Move the pointer that is the bottleneck (shorter wall, smaller max)
- Fix one element + two pointers reduces O(n²) brute force to O(n) or O(n²) from O(n³)
- Always ask: what do I calculate each step? which pointer moves and why?

### Stack
- Stack = list in Python. Push with append(), pop with pop(), peek with [-1]
- Use when you need to match pairs or track previous state
- Always check if stack is empty before popping
- After the loop, check if stack is empty — leftover items mean unmatched elements
- Never return True inside a loop prematurely — only return False on mismatch
