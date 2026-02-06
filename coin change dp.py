coins = [1,3,4]
amount = 6

dp = [float('inf')]*(amount+1)
dp = 0

for coin in coins:
    for i in range(1,amount+1):
        dp[i] = min(dp[i],dp[i-coin]+1)

if dp[amount] == float('inf'):
    print(-1)
else:
    print(dp[amount])