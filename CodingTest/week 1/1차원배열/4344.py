c = int(input())

for i in range(0, c):
    a = []
    count = 0
    sum = 0

    a = list(map(int, input().split()))
    for i in range(1, len(a)):
        sum += a[i]
    avg = sum / a[0]

    for i in range(1, len(a)):
        if(a[i] > avg):
            count += 1
    print("%.3f%%" %(count/a[0]*100))