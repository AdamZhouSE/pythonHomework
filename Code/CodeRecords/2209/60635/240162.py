num = int(input())
target = input()
words = []

for i in range(0, num):
    words.append(input())

words.sort(key=lambda x: len(x), reverse=True)
maxLen = len(words[0])
minLen = len(words[-1])

count = 0
curr = 0  # 已经拼好的长度
i = 0  # 游标
alphaset=set(''.join(words))
if len(alphaset)==26:
    print(len(target))
else:
    while i < len(target):
        for j in range(maxLen, minLen - 1, -1):
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
        i -= 1  # i不能后退太多 即重叠的部分不能长于maxlen
        if i < curr - maxLen:
            break
    if curr >= len(target):
        print(count)
    else:
        print(-1)
