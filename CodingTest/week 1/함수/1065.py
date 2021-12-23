n = int(input())
count = 0
numbers = []

for i in range(1, n+1):
    if(i <= 99):
        count += 1
    else:
        n = list(map(int, str(i)))
        if(n[0] - n[1] == n[1] - n[2]):
            count += 1

print(count)