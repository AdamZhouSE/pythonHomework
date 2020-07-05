# 题目描述
# 给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数。

def isOK(num) -> bool:
    string = list(str(num))
    if len(string) > 10:
        return True
    sset = set(string)
    return not len(string) == len(sset)

if __name__ == '__main__':
    cnt = 0
    n = int(input())
    for i in range(1, n+1):
        if isOK(i):
            cnt += 1
    print(cnt)