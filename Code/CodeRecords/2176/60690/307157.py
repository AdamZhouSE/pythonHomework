s=input()
ss=[]
sss=[]
for i in range(len(s)):
    ss.append(s[i])
    sss.append(s[i])
res=[]
ss.sort()
for i in range(len(ss)):
    for j in range(len(sss)-1,-1,-1):
        if sss[j]==ss[i]:
            res.append(j+1)
            sss[j]=''
for i in range(len(res)-1):print(res[i],end=" ")
print(res[-1])