n = int(input())

a = list(map(int, input().split()))
a.sort()

b = []
sum = 0

for i in range(0, n):
    b.append(a[i]/a[n-1]*100)
    sum += b[i]

print(sum/n)