# 读题的意思 后缀数组自己了解 https://blog.csdn.net/yxuanwkeith/article/details/50636898
# sa[i]  = j 表示排名第i的后缀字符串的开头字符在原字符串的第j位
# rank[i] = j 原字符串的第i个后缀字符串，排名为j
def cal(s):
    strs = []
    res = []
    for i in range(len(s)):
        strs.append(s[i:])
    temp = strs.copy()
    strs.sort()
    for i in strs:
        res.append(str(temp.index(i)+1))
    return " ".join(res)


print(cal(input()),end =" ")