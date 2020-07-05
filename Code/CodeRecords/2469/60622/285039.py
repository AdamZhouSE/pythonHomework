def getKey(c):
    return len(c)
n=int(input())

for i in range(n):
    l=list(input())
    s=list(set(l))
    ans=[]
    for i in range(0,len(l)-len(s)+1):
        for j in range(i+len(s),len(l)+1):
            check=l[i:j]
            isAllIn=True
            for e in s:
                if e not in check:
                    isAllIn=False
                    break
            if isAllIn:
                ans.append(check)
    ans=sorted(ans,key=getKey)
    print(len(ans[0]))