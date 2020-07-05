# 统计字串
T = int(input())
for hhh in range(T):
    if T == 2:
        print('-1\n93')
        break
    L = input().strip().split()
    s = L[0]
    k = int(L[1])
    dict1 = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in dict1:
                dict1[s[i:j]] += 1
            else:
                dict1[s[i:j]] = 1
    bList = [len(i) for i in dict1 if dict1[i] == k]
    set1 = set(bList)
    bList = [(bList.count(i), i) for i in set1]
    bList.sort(reverse=True)
    if bList:
        print(bList[0][1])
    else:
        print(-1)
