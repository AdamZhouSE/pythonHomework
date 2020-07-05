source=eval(input())
k=int(input())
print(source)
print(k)
res=[]
for i in range(len(source)):
    sums=0
    a=i
    while(sums<k):
        sums=sums+source[a]
        a=a+1
        if a==len(source) and sums<k:
            break
    if(a==len(source)):
        res.append(-1)
    else:
        res.append(a-i)
while(-1 in res):
    res.pop(res.index(-1))
if(len(res)==0):
    print(-1)
else:
    print(min(res))