def needtodo(l,r):
    ll=chr(l)
    rr=chr(r)
    if ((ll>='0')and(ll<='9')and(rr>='0')and(rr<='9')):
        return True
    elif (((ll>='a')and(ll<='z'))or((ll>='A')and(ll<='Z')))and(((rr>='a')and(rr<='z'))or((rr>='A')and(rr<='Z'))):
        return True
    return False

p1,p2,p3=map(int,input().split())
strs=input().split('-')
print(strs)
ans=strs[0]
for i in range(1,len(strs)):
    l=ord(ans[len(ans)-1])
    r=ord(strs[i][0])
    if needtodo(l,r):
        tmp=""
        for j in range(l+1,r):
            for k in range(0,p2):
                if p1==3:
                    tmp+='*'
                else:
                    tmp+=chr(j)
        if p1==1:
            tmp=tmp.lower()
        elif p2==2:
            tmp=tmp.upper()
        if p3==2:
            tmp="".join(reversed(str))
        ans+=tmp
    else:
        ans+='-'
    ans+=strs[i]
print(ans)