a, b = map(int, input().split())

b = b - 45

if(b < 0):
    a = a - 1
    if(a < 0):
        a = 24 + a
    b = 60 + b
else:
    if(a < 0):
        a = 24 - 1

print(a, b)