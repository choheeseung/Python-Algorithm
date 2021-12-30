n = int(input())
a = list(map(int, input().split()))
count = 0

for i in a:
    k = 0
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            k += 1
    if k == 1:
        count += 1

print(count)
