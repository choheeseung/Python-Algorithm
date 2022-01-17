import sys

num = sys.stdin.readline()
tempn = int(num)
count = 0

while True:
    # num이 10이하일 때
    if(tempn < 10):
        a = 0
        b = tempn
    # a에 십의자리 수를, b에 일의자리 수를 넣는다.
    a = tempn // 10
    b = tempn % 10
    # 임의의 변수 t에 a를 넣고 십의자리에는 b를,
    # 일의자리에는 십의자리수와 일의자리수를 합한 값을 넣는다.
    t = a
    a = b
    b = t+b
    if(b >= 10):
        b = b % 10
    tempn = 10*a+b
    count += 1
    # 원래의 수로 돌아올 때까지 반복하고,
    # 만약 같으면 몇 번 반복했는지 출력한다.
    if(tempn == int(num)):
        print(count)
        exit(0)
