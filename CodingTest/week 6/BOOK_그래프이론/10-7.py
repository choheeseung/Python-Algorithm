# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


n, m = map(int, input().split())

for i in range(m):
    oper, a, b = map(int, input().split())
