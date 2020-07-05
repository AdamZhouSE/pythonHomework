a=input().split(',')

res=[]
for i in range(len(a)):
    a[i]=int(a[i])
#print(a)
for i in range(len(a)):
    if a[i]<=len(a)-i:
        res.append(a[i])
res.sort()
print(res[-1])
