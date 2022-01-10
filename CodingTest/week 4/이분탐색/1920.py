def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a_sort = sorted(a)

for i in b:
    result = binary_search(a_sort, i, 0, n - 1)
    if result != None:
        print("1")
    else:
        print("0")
