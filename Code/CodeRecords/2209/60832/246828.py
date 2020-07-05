num = int(input())
target = input()
words = []

for i in range(0, num):
    words.append(input())

words.sort(key=lambda x: len(x), reverse=True)
len_set=list({len(x) for x in words})
len_set.sort(reverse=True)

count = 0
curr = 0  # 已经拼好的长度
i = 0  # 游标

while i < len(target):
    for j in len_set:
        if i + j <= curr:
            break
        test = target[i:i+j]  # 超出部分自动忽略
        if test in words:
            count += 1
            curr = i + j
            i = curr + 1
            break
        if curr < i:
            break
    if curr >= len(target):
        break
    i -= 1  # i不能后退太多 即重叠的部分不能长于最大长度
    if i < curr - len_set[0]:
        break
if curr >= len(target):
    print(count)
else:
    print(-1)