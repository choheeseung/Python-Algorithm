a, b = input().split()

a_list = int(a[::-1])  # 처음부터 끝까지 -1칸 간격으로(=역순으로)
b_list = int(b[::-1])

if a_list > b_list:
    print(a_list)
else:
    print(b_list)
