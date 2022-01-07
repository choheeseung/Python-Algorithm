def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n = int(input())

graph = []
danji = []
count = 0

for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            danji.append(count)
            count = 0

danji.sort()
print(result)
for i in range(len(danji)):
    print(danji[i])
