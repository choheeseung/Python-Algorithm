import sys

num = sys.stdin.readline()
tempn = int(num)
count = 0

while True:
    if(tempn<10):
        a = 0
        b = tempn
    a = tempn // 10
    b = tempn % 10
    t = a
    a = b
    b = t+b
    if(b >= 10):
        b = b % 10
    tempn = 10*a+b
    count += 1
    if(tempn == int(num)):
        print(count)
        exit(0)