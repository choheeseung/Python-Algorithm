a = input()
b = input()

c = list(b) #공백을 포함하여 한 문자씩 모두 나눔

x = int(a) * int(c[2])
y = int(a) * int(c[1])
z = int(a) * int(c[0])

print(x)
print(y)
print(z)
print(x + 10 * y + 100 * z)