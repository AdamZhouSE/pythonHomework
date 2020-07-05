'''
给定一个单词数组，按排序顺序（计数的递增顺序）一起打印所有字符相同组的计数。
例如，如果给定的数组是{“ cat”，“ dog”，“ tac”，“ god”，“ act”}，
则分组的字谜是“（dog，god）（cat，tac，act）”。因此输出为2 3
'''


def isIn(c, diff):
    for tmp in diff:
        if c == tmp:
            return True
    return False


def getAllDiff(word):
    diff = []
    for c in word:
        if isIn(c, diff):
            continue
        else:
            diff.append(c)
    diff = ''.join(sorted(diff))
    return diff


def groupNum(words):
    all_group = []
    count = []

    for word in words:
        tmp = ''.join(sorted(word))
        if isIn(tmp, all_group):
            continue
        else:
            all_group.append(tmp)

    for i in range(0, len(all_group)):
        count.append(2)
        for j in range(0, len(words)):
            if all_group[i] == words[j]:
                count[i] += 1

    count.sort()
    for i in range(0, len(count) - 1):
        print(count[i], end=' ')
    print(count[-1])


t = int(input())
for i in range(0, t):
    n = int(input())
    words = input().split(' ')
    groupNum(words)
