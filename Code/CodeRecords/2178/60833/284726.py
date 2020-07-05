def cut(s: str):
    results = []
    num = 0
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return len(results)
n=int(input())
num_str=input().split(" ")
str1=""
res=0
for i in num_str:
    str1+=i
    print(cut(str1)-res)
    res=cut(str1)