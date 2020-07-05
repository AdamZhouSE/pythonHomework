import collections
def characterReplacement(s,k):
    res=0
    l=0
    mf=0
    a=list(s)
    alls=[]
    for i in a:
        if(not i in alls):
            alls.append(i)
    count=[]
    for i in alls:
        count.append(0)
    d = collections.defaultdict(int)
    for r in range(len(a)):
        d[a[r]]=d[a[r]]+1
        count[alls.index(a[r])]=count[alls.index(a[r])]+1
        mf = max(mf, d[a[r]])
        while r - l + 1 - mf > k:
            d[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
s=input()
k=int(input())
print(characterReplacement(s,k))