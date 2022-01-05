import sys

n = int(sys.stdin.readline())

xy = [[0] * 2 for _ in range(n)]
for i in range(n):
    xy[i][0], xy[i][1] = map(int, sys.stdin.readline().split())

xy.sort()

for i in range(n):
    print(xy[i][0], xy[i][1])
