t=int(input())
for tt in range(t):
    s=input()
    ans=-1
    beg={}
    for i in range(len(s)):
        if(s[i] in beg):
            ans=max(ans,i-beg[s[i]]-1)
        else:
            beg[s[i]]=i
    print(ans)