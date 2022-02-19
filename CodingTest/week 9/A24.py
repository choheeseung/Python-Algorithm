# 정렬 문제 - 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1) // 2])
