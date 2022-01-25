n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = array[0][0]

for i in range(1, n):
    for j in range(len(array[i])):
        if j == 0:
            dp[i][j] = array[i][j] + dp[i-1][j]
        elif j == len(array[i]) - 1:
            dp[i][j] = array[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]

print(max(dp[n-1]))
