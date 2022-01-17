t = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1

for i in range(t):
    n = int(input())

    for j in range(3, n+1):
        dp[j] = dp[j-2] + dp[j-3]

    print(dp[n])
