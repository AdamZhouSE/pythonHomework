def cut(s: str):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results
def solve(s:str,st:str):
    re = cut(s)
    Min = len(s)
    for i in re:
        isOk = True
        for j in st:
            if j not in i:
                isOk = False
                break
        if isOk:
            Min = min(Min,len(i))
    return Min

n = eval(input())
for i in range(n):
    s = input()
    st = ''.join(list(set(list(s))))
    print(solve(s,st))
