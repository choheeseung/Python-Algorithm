a = []

for i in range(0, 10):
    n = int(input())
    a.append(n % 42)

#set은 중복없고 순서도 없는 집합 자료형을 만든다
a = set(a)
print(len(a))
