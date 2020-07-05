from collections import Counter
T=int(input())
res=[]
def getmin(s,t):
    dict=Counter(t)
    req=len(dict)
    l,r,formed=0,0,0
    window={}
    ans=float("inf"),None,None
    while r<len(s):
        c=s[r]
        window[c]=window.get(c,0)+1
        if c in dict and window[c]==dict[c]:
            formed+=1
        while l<=r and formed==req:
            c=s[l]
            if r-l+1<ans[0]:
                ans=(r-l+1,l,r)
            window[c]-=1
            if c in dict and window[c]<dict[c]:
                formed-=1
            l+=1
        r+=1
    return ans[2]-ans[1]+1

for i in range(T):
    s=input()
    min=len(s)
    t="".join(set(s))
    res.append(getmin(s,t))
for i in range(T):
    print(res[i])
