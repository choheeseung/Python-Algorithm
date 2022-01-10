def binary_search(num, bound):
    start, end = 0, n
    while start < end:
        mid = (start + end) // 2
        if bound == 0:
            if n_list[mid] < num:
                start = mid + 1
            else:
                end = mid
        else:
            if n_list[mid] <= num:
                start = mid + 1
            else:
                end = mid
    return end


n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

result = []
for i in m_list:
    result.append(binary_search(i, 1) - binary_search(i, 0))

print(*result)
