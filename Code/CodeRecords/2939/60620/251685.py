k,m=map(int,input().split())
c=0
a=[1]
b=[]
while(c<k):
    x=min(a)
    b.append(x)
    a.remove(x)
    a.append(2*x+1)
    a.append(4*x+5)
    c+=1
b=sorted(b)
l1=[str(i) for i in b]
r1="".join(l1)
print(r1)
l=[int(i) for i in r1]
index=l.index(max(l))
l2=[]
if(m==index):
    l2.extend(l[index:])
elif(m>index):
    l2.append(l[index])
    for i in range(m-index+1):
        l.remove(min(l[index:]))
    l2.extend(l[index:])
else:
    for i in range(m):
        l.remove(min(l[:index]))
    l2.extend(l)
r2=[str(i) for i in l2]
print("".join(r2),end="")

