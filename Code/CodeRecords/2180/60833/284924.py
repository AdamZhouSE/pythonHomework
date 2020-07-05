def cut(s: str):
    results = []
    num = 0
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results
str1=str(input())
str2=str(input())
res1=cut(str1)
res2=cut(str2)
res=0
for i in res1:
    res+=str2.count(i)
print(res,end="")