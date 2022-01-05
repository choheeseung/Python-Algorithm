import sys

n = int(sys.stdin.readline())
array = list(map(int, (sys.stdin.readline().split())))

array2 = sorted(list(set(array)))
dic = {array2[i]: i for i in range(len(array2))}

for i in array:
    print(dic[i], end=" ")
