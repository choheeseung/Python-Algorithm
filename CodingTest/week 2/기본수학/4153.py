while 1:
    a, b, c = map(int, input().split())
    if a == 0 & b == 0 & c == 0:
        exit(0)
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        print("right")
    elif pow(a, 2) + pow(c, 2) == pow(b, 2):
        print("right")
    elif pow(b, 2) + pow(c, 2) == pow(a, 2):
        print("right")
    else:
        print("wrong")
