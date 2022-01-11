n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    total = sum(i - mid if i - mid > 0 else 0 for i in array)
    if total < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)
