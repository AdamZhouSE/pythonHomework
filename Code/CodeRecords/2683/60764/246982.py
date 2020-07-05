def findWay(path,s,ind,res):
    if ind==len(s)-1:
        res.append(len(path))
        return
    if max(s[ind+1:len(s)])<=s[ind]:
        res.append(len(path))
        return
    for i in range(ind+1,len(s)):
        if s[i]>s[ind]:
            pathc=path.copy()
            pathc.append(s[i])
            findWay(pathc,s,i,res)

T=int(input())
for t in range(T):
    s=list(input())
    res=[]
    for i in range(len(s)):
        findWay([s[i]],s,i,res)
    print(max(res))