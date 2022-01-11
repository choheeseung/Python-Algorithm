n, c = map(int, input().split())

x = []
for i in range(n):
    x.append(int(input()))

x.sort()
start = 1
end = x[-1] - x[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    old = x[0] #배열의 가장 낮은 좌표
    count = 1

    for i in range(1, len(x)):
        if x[i] >= old + mid:
            count += 1
            old = x[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
