a = int(input())
b = int(input())
c = int(input())

#""안에 들어있는 문자열(str)은 list를 사용해서 리스트로 변형하면
# 0부터 각각의 index로 저장된다.
mul = list(str(a*b*c))

for i in range(10):
    print(mul.count(str(i)))