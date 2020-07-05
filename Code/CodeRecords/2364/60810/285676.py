'''
给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数。
'''

def isRepeat(a):
    string = []
    while a > 0:
        temp = a % 10
        string.append(temp)
        a //= 10

    for i in range(0, len(string)-1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return True
    return False

n = int(input())
if n <= 10:
    print(0)
else:
    count = 0
    for i in range(11, n+1):
        if (isRepeat(i)):
            count += 1
    print(count)
