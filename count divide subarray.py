numbers = [2,5,4,6,2,1]

n = len(numbers)
dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if numbers[i]%numbers[j]==0:
            dp[i] = dp[i] + dp[j]

print(sum(dp))