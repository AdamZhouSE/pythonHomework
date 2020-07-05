# 辅助函数：若列表中有多种字符，计算对于每种字符来说，列表中非此字符的个数
# 返回个数的最小值


def support(x: list) -> int:
    chars = list(set(x))
    res = len(x)
    for i in chars:
        tmp = len(x) - x.count(i)
        if tmp < res:
            res = tmp
    return res


s = list(input())
k = int(input())
result = 0
for i in range(len(s), 0, -1):
    chanceLeft = k
    subString = []
    find = False
    # for j in range(i + 1, len(s)):
    for j in range(0, len(s) - i + 1):
        subString = s[j:j+i]
        if support(subString) == k:
            find = True
            break
    if find and len(subString) > result:
        result = len(subString)
print(result)
