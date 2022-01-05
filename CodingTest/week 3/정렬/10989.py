import sys

n = int(sys.stdin.readline())

count = [0] * 10001

for i in range(n):
    input_num = int(sys.stdin.readline())
    count[input_num] = count[input_num] + 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
