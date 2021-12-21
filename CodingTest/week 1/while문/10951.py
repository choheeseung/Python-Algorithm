import sys

while True:
    #try 수행 중 오류가 발생하면 except 블록이 수행된다.
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break