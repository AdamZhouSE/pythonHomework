s=input()[1:-1].split(",")
for i in range(len(s)): s[i]=int(s[i])
res=[]
for i in range(len(s)-1):
    count=0
    for j in range(i+1,len(s)):
        if s[i]>s[j]: count+=1
    res.append(count)
res.append(0)
print(res)