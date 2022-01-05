import sys
from typing import Counter

n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

sum = 0
for i in range(len(array)):
    sum += array[i]

print(round(sum / n))
print(array[int(n / 2)])

cnt = Counter(array).most_common(2)

if len(array) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(array[n - 1] - array[0])
