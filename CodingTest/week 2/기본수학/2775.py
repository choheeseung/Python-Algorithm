person = [[0] * 15 for i in range(15)]

for i in range(0, 15):
    for j in range(0, 15):
        person[0][j] = j
        person[i][1] = 1
        person[i][j] = person[i][j - 1] + person[i - 1][j]

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    print(person[k][n])
