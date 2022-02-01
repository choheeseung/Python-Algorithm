t = int(input())

for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    table = [[0] * (n+1) for _ in range(n+1)]

    for j in range(n-1):
        table[j][j+1] = data[j] + data[j+1]
        for l in range(j+2, n):
            table[j][l] = table[j][l-1] + data[l]

    for v in range(2, n):
        for w in range(n-v):
            j = w+v
            table[w][j] += min([table[w][k] + table[k+1][j]
                               for k in range(w, j)])

    print(table[0][n-1])
