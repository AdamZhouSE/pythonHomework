#28
# 不是简单的排序就可以解决的，后面可能有些人注定无法满意，不如让他拍到后面，让有耐心的人先来
# 例如 1 3 5 7 9 按照排序来看，似乎只有1 3 5可以满意 但事实上，1 3 5 9 7就是四个人满意了
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
num.sort()
satisfy = []
satisfy.append(num[0])
while True:
    sum_all = 0
    isEnd = True
    for item in satisfy:
        sum_all += item
    for i in range(len(satisfy),n):
        if num[i] >= sum_all:
            isEnd = False
            satisfy.append(num[i])
            break
    if isEnd:
        break
print(len(satisfy))