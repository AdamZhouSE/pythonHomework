a=eval(input())
k=int(input())
r=[]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if(sum(a[i:j])>=k):
            r.append(a[i:j])
l=len(a)            
for i in r:
    l=min(len(i),l)
if(r==[]):
    print(-1)
else:
    print(l)