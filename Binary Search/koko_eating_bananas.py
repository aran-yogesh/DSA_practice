# ============================================================
# 875. Koko Eating Bananas
# Difficulty: Medium
#
# Problem:
# Koko has n piles of bananas. Guards return in h hours.
# She eats k bananas/hour from one pile. If pile < k, she
# eats the whole pile in that hour. Return minimum k such
# that she finishes all bananas within h hours.
#
# Example 1:
#   Input:  piles = [3,6,7,11], h = 8    Output: 4
# Example 2:
#   Input:  piles = [30,11,23,4,20], h = 5   Output: 30
# Example 3:
#   Input:  piles = [30,11,23,4,20], h = 6   Output: 23
# ============================================================

# ---- Algorithm ----
# 1. Binary search between l=1 and r=max(piles)
#    - l=1 is the slowest possible speed
#    - r=max(piles) is the fastest useful speed (eating biggest pile in 1 hour)
# 2. For each mid (candidate speed k), calculate total hours:
#    hours = sum(ceil(pile/mid) for each pile)
# 3. If total hours <= h → valid speed, try slower → r = mid - 1
# 4. If total hours > h  → too slow, need faster  → l = mid + 1
# 5. Return l — the minimum valid speed

import math


def minEatingSpeed(piles, h):
    l = 1
    r = max(piles)

    while l <= r:
        mid = (l + r) // 2
        hours = sum(math.ceil(pile / mid) for pile in piles)

        if hours <= h:
            r = mid - 1     # valid speed, try slower
        else:
            l = mid + 1     # too slow, need faster

    return l                # minimum valid speed


# ============================================================
# Dry Run: piles = [3,6,7,11], h = 8
# l=1, r=11
#
# Step 1: mid=6
#   hours = ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) = 1+1+2+2 = 6
#   6 <= 8 → valid, try slower → r=5
#
# Step 2: mid=3
#   hours = ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3) = 1+2+3+4 = 10
#   10 > 8 → too slow → l=4
#
# Step 3: mid=4
#   hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8
#   8 <= 8 → valid, try slower → r=3
#
# l=4 > r=3 → loop ends → return l=4 ✓
#
# Time Complexity:  O(n log m) — log m binary search steps, n piles per step
#                  n = number of piles, m = max(piles)
# Space Complexity: O(1) — only pointers and running sum, no extra storage
#                  Note: sum() generator computes on the fly, stores nothing
# ============================================================

# ---- Key Insight ----
# k is NOT given — it's what we're searching for!
# Binary search on the ANSWER (k) instead of on the input array.
# Search space is 1 to max(piles) — no point eating faster than biggest pile.
# For each candidate k (mid), check if it works in <= h hours.

# ---- Tradeoffs ----
# This approach (binary search on the answer):
#   O(n log m) time — n piles per check, log m search steps (m = max pile)
#   O(1) space — generator computes hours on the fly, no extra storage
#   Pro: Hugely faster than brute force when max pile is large
#
# Brute force alternative:
#   Try every k from 1 to max(piles) → O(n * max(piles)) time
#   Way too slow when max(piles) reaches 10^9
#
# Binary search on answer pattern: when the answer is a value in a range
# AND checking a candidate is easy (O(n) here), binary search over that range

# ---- Where I Needed Assistance ----
# 1. What k is — it's the eating speed = mid in binary search
#    Fix: we're binary searching on the answer, not the input
#
# 2. Search space boundaries:
#    l=1 (minimum speed), r=max(piles) (no point going faster)
#
# 3. ceil syntax — math.ceil(pile/mid) or (pile + mid - 1) // mid
#    Fix: import math and use math.ceil()
#
# 4. How to compute total hours for all piles:
#    sum(math.ceil(pile/mid) for pile in piles)
#
# 5. Condition direction:
#    hours <= h → valid, try slower → r = mid - 1
#    hours > h  → too slow → l = mid + 1
#
# ---- What to Improve ----
# - "Binary search on the answer" is a powerful pattern:
#   when you're finding the minimum/maximum value that satisfies a condition
# - Always ask: what is the search space? (here: 1 to max(piles))
# - Always ask: what condition makes a candidate valid? (here: hours <= h)
# - Space complexity: generators and for loops don't store data → O(1)


if __name__ == "__main__":
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ]

    for piles, h, expected in test_cases:
        output = minEatingSpeed(piles, h)
        print(f"Input:    piles={piles}, h={h}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
