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
    for r, c in enumerate(s):
        d[c]=d[c]+1
        print(d)
        count[alls.index(a[r])]=count[alls.index(a[r])]+1
        print(count)
        mf = max(mf, d[c])
        while r - l + 1 - mf > k:
            d[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
s=input()
k=int(input())
print(characterReplacement(s,k))