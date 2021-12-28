a = list(input())
Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
count = 0

for i in a:
    if i in Alphabet[0:3]:
        count += 3
    elif i in Alphabet[3:6]:
        count += 4
    elif i in Alphabet[6:9]:
        count += 5
    elif i in Alphabet[9:12]:
        count += 6
    elif i in Alphabet[12:15]:
        count += 7
    elif i in Alphabet[15:19]:
        count += 8
    elif i in Alphabet[19:22]:
        count += 9
    else:
        count += 10

print(count)
