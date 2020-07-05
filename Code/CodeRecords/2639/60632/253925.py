# 辅助函数：若列表中有多种字符，计算对于每种字符来说，列表中非此字符的个数
# 返回个数的最小值


def support(x: list) -> int:
    chars = list(set(s))
    result = len(x)
    for i in chars:
        tmp = len(x) - x.count(i)
        if tmp < result:
            result = tmp
    return result


s = list(input())
k = int(input())
result = len(s)
for i in range(len(s)):
    chanceLeft = k
    subString = [s[i]]
    for j in range(i + 1, len(s)):
        subString.append(s[j])
        if support(subString):
            break
    if len(subString) < result:
        result = len(subString)
print(result)
