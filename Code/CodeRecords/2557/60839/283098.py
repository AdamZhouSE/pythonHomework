def delletter(s):
    st=list(s)
    ans=""
    ans=ans+st[0]
    for i in range(0,len(st)-1):
        if st[i]!=st[i+1]:
            ans=ans+st[i+1]
    return ans


n=int(input())
s=[]
for i in range(0,n):
    s.append(delletter(input()))
    ##print(s[i])

for i in range(0,n):
    print(s[i])