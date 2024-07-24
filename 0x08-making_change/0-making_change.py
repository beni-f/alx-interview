#!/usr/bin/python3
"""
0-making_change
"""


def makeChange(coins, total):
    """
        Determine the fewest number of coins needed to meet a given amout total
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] <= total else -1
