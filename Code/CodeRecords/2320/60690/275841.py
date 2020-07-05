s=input()
k=int(input())
form=s[0:k]
res=""
l1=[]
for e in form: l1.append(e)
if k<len(s):
    after=s[k:]  
    l2=[]
    for e in after: l2.append(e)
    while max(l1)>min(l2):
        temp=max(l1)
        l1.pop(l1.index(max(l1)))
        l1.append(l2[0])
        for i in range(len(l2)-1):
            l2[i]=l2[i+1]
        l2[-1]=temp
    l1.sort()
    for e in l1:res+=e
    for e in l2:res+=e
else:
    l1.sort()
    for e in l1:res+=e
print(res)
