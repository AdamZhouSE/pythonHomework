n=input().split(',')
for i in range(len(n)):
    n[i]=int(n[i])
n.sort()
res=[]
res.append(n[0])
for i in range(1,len(n)):
    #print(res)
    j=True
    for j in res:
        if n[i]%j!=0 and j%n[i]!=0:
            j=False
    if j:
        res.append(n[i])
            
print(res)
