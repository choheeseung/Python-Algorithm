x = int(input())
line = 0  # 지그재그에서 몇번째라인
max_num = 0

while x > max_num:
    line += 1
    max_num += line

diff = max_num - x

# 짝수라인은 분자+1, 분모-1씩
# 홀수라인은 분자-1, 분모+1씩
if line % 2 == 0:
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d" % (top, bottom))
