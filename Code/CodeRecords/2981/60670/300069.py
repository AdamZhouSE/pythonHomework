p1,p2,p3=map(int,input().split())
strs=input().split('-')
ans=strs[0]
for i in range(1,len(strs)):
    l=ord(ans[len(ans)-1])
    r=ord(strs[i][0])
    tmp=""
    for j in range(l+1,r):
        for k in range(0,p2):
            tmp+=chr(j)
    if p1==1:
        tmp=tmp.lower()
    else:
        tmp=tmp.upper()
    if p3==2:
        tmp="".join(reversed(str))
print(ans)