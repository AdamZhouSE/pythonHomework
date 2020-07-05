def cut(s: str):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    results = list(set(results))
    # re = []
    # for index in results:
    #     if index == index[::-1]:
    #         re.append(index)
    return results

n = eval(input())

s = input()

result = 0
for i in range(1,n):
    sA = s[0:i]
    sB = s[i:]
    listA = cut(sA)
    listB = cut(sB)
    nA = 0
    nB = 0
    for i in listA:
        if len(i)%2!=0 and i==i[::-1] :
            nA = nA + 1
    for i in listB:
        if len(i)%2!=0 and i==i[::-1]:
            continue
        else:nB = nB + 1
    #nB = len(listB)
    result = max(result,nA*nB)
print(result)

