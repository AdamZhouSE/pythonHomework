from itertools import combinations

s = input().lstrip(')').rstrip('(')
lp = s.count('(')
rp = s.count(')')
if(lp == rp):
    print(s)
else:
    limit = 0
    deletable = []
    if(lp < rp):
        rpD = []
        safe = len(s)
        for i in range(s.rfind(')'),-1,-1):
            if(s[i] == ')'):
                limit = limit + 1
            elif(s[i] == '('):
                limit = limit - 1
            if(limit == 0):
                safe = i
                break
        for j in range(0,safe):
            if(s[j] == ')'):
                rpD.append(j)
        deletable = list(combinations(rpD,rp - lp))
    else:
        lpD = []
        safe = 0
        for i in range(0,len(s)):
            if(s[i] == '('):
                limit = limit + 1
            elif(s[i] == ')'):
                limit = limit - 1
            if(limit == 0):
                safe = i
                break
        for j in range(safe,len(s)):
            if(s[j] == '('):
                lpD.append(j)
        deletable = list(combinations(lpD,lp - rp))
    res = []
    for item in deletable:
        temp = s
        for i in range(len(item) - 1,-1,-1):
            temp = temp[:item[i]] + temp[item[i] + 1:]
        res.append(temp)
    res = list(set(res))
    print(res)
    