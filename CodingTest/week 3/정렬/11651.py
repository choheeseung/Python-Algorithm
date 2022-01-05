import sys

n = int(sys.stdin.readline())

xy = [[0] * 2 for _ in range(n)]
for i in range(n):
    xy[i][0], xy[i][1] = map(int, sys.stdin.readline().split())

xy.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(xy[i][0], xy[i][1])
