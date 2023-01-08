from typing import List

#recursive
def coinChangeR(coins: List[int], amount: int) -> int:
    def countCoins(amount):
        print(amount, end=" ")
        if amount == 0:
            return 0

        if amount < 0:
            return 10**4 + 1
        
        count = 10**4 + 1

        for c in coins:
            count = min(count, countCoins(amount - c))
            print(count, end="    ")
        return count + 1

    return countCoins(amount) if countCoins(amount) <= 10**4 + 1 else -1

#dp
def coinChange(coins: List[int], amount: int) -> int:
    dp = [10**4 + 1] * (amount + 1)
    dp[0] = 0
    for amt in range(amount + 1):
        for c in coins:
            if amt - c < 0:
                continue
            dp[amt] = min(dp[amt], dp[amt - c] + 1)
    return dp[amount] if dp[amount] < 10**4 + 1 else -1