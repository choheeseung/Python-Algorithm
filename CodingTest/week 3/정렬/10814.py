import sys

n = int(sys.stdin.readline())
member = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member.append((age, name))

member.sort(key=lambda member: member[0])

for i in range(n):
    print(member[i][0], member[i][1])
