s=input()
pro=[]
res=[]
for i in range(len(s)):
    pro.append(s[i:len(s)])
pro.sort()
for i in range(len(pro)):
    res.append(len(s)-len(pro[i])+1)
print(' '.join(str(r) for r in res))