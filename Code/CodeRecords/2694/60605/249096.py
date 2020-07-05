# 题目描述
# 给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。
#
# 返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）
#
# 输入描述
# 一个字符串 S。
# 2 <= S.length <= 10^5
# S 由小写英文字母组成。
# 输出描述
# 返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）

def lenTwoStr(str1, str2) -> int:
    if len(str1) == 0 or len(str2) == 0: return 0
    i = 0
    while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
        i+=1
    return i

def solve() -> str:
    s = input()
    leng = len(s)
    res = ""
    maxlen = 0
    if leng <= 1:
        return ""
    strs = []
    for i in range(leng):
        strs.append(s[i: leng])

    strs = sorted(strs)
    for i in range(0, leng-1):
        tmp = lenTwoStr(strs[i], strs[i+1])
        if tmp > maxlen:
            maxlen = tmp
            res = strs[i][0:maxlen]
    return res


print(solve())

