# 에라토스테네스의 체 이용
def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


m, n = map(int, input().split())

for k in range(m, n + 1):
    if isPrime(k):
        print(k)
