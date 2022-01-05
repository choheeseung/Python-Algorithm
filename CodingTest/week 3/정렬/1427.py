num = input()

array = list(num)
array = list(map(int, array))

array.sort(reverse=True)

for i in range(len(array)):
    print(array[i], end="")
