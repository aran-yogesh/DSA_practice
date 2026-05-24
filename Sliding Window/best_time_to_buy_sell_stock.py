# ============================================================
# 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
#
# Problem:
# Given an array prices where prices[i] is the stock price on
# day i, return the maximum profit from one buy and one sell.
# You must buy before you sell. Return 0 if no profit possible.
#
# Example 1:
#   Input:  prices = [7,1,5,3,6,4]   Output: 5
#   Explanation: Buy day 2 (price=1), sell day 5 (price=6)
#
# Example 2:
#   Input:  prices = [7,6,4,3,1]     Output: 0
#   Explanation: Prices only decrease, no profit possible
# ============================================================

# ---- Strategy: Sliding Window (Two Pointers) ----
# l = buy day, r = sell day
# r scans every day one by one.
# If prices[r] < prices[l] → found a cheaper buy day → move l to r
# Otherwise → calculate profit and update best
# Start best=0 so if no profit is ever found, we return 0.

from typing import List


def maxProfit(prices: List[int]) -> int:
    best = 0
    l = 0

    for r in range(len(prices)):
        if prices[r] < prices[l]:
            l = r                               # cheaper buy day found
        else:
            best = max(best, prices[r] - prices[l])  # update max profit

    return best


# ============================================================
# Dry Run: prices = [7, 1, 5, 3, 6, 4]
# l=0, best=0
#
# r=0: prices[0]=7, 7 < 7? No  → best=max(0, 7-7)=0
# r=1: prices[1]=1, 1 < 7? Yes → l=1
# r=2: prices[2]=5, 5 < 1? No  → best=max(0, 5-1)=4
# r=3: prices[3]=3, 3 < 1? No  → best=max(4, 3-1)=4
# r=4: prices[4]=6, 6 < 1? No  → best=max(4, 6-1)=5
# r=5: prices[5]=4, 4 < 1? No  → best=max(5, 4-1)=5
#
# return 5 ✓
#
# Dry Run: prices = [7, 6, 4, 3, 1]
#
# r=0: 7<7? No  → best=0
# r=1: 6<7? Yes → l=1
# r=2: 4<6? Yes → l=2
# r=3: 3<4? Yes → l=3
# r=4: 1<3? Yes → l=4
#
# return 0 ✓
#
# Time Complexity:  O(n) — single pass, r visits each element once
# Space Complexity: O(1) — only l, r, best — no extra data structure
# ============================================================

# ---- Tradeoffs ----
# This approach (two pointers):
#   Pro: O(n) time, O(1) space — optimal
#   Simple logic — just track cheapest buy seen so far
#
# Brute force (check every pair):
#   O(n²) time — try every buy/sell combination
#   Too slow for large inputs
#
# Why l = r and not l += 1:
#   When prices[r] < prices[l], r is the new cheapest price seen
#   Jumping l to r means we buy at the cheapest point found so far
#   Moving l += 1 would miss the cheaper price at r

# ---- Self Reflection: Where I got stuck ----
# 1. l = 0 inside the loop — reset l every iteration, broke the logic
#    Fix: l and best must be initialised OUTSIDE the loop
#
# 2. l = r vs l += 1 — wasn't sure how far to move l
#    Fix: when prices[r] is cheaper, jump l all the way to r
#         r is now the best buy day, not just one step ahead
#
# 3. Visualisation — hard to see without tracing
#    Fix: dry run 3-4 steps on paper before coding
#         trace l, r, best manually — no need to see it in your head

# ---- What to Improve ----
# - Always initialise l and best OUTSIDE the for loop
# - Sliding window pattern: for loop for r, control l manually inside
# - When you find a cheaper left boundary, jump l there directly
# - Dry run habit: trace 3-4 steps before coding — replaces visualisation


if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1], 0),
    ]

    for prices, expected in test_cases:
        output = maxProfit(prices)
        print(f"Input:    {prices}")
        print(f"Output:   {output}")
        print(f"Expected: {expected}")
        print(f"Pass:     {output == expected}")
        print()
