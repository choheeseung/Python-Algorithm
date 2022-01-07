def dfs(v):
    visit[v] = 1
    for i in range(n):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]
visit = [0 for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = graph[b - 1][a - 1] = 1

dfs(0)

cnt = 0
for i in range(1, n):
    if visit[i] == 1:
        cnt += 1

print(cnt)
