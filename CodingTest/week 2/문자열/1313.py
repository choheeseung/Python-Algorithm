num = int(input())
group = 0

for i in range(num):
    voca = input()
    err = 0
    for i in range(len(voca) - 1):
        if voca[i] != voca[i + 1]:
            new_word = voca[i + 1 :]
            # count는 문자열 내부에서 특정 문자 혹은 문자열이
            # 포함되어있는지 계산해서 반환해주는 함수
            if new_word.count(voca[i]) > 0:
                err += 1
    if err == 0:
        group += 1

print(group)
