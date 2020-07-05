n=int(input())
a=input().split()
a=list(map(int,a))
k1=a.pop(0)
oa=a[:]
b=input().split()
b=list(map(int,b))
k2=b.pop(0)
ob=b[:]
cnt=0
e=True
while len(a)>0 and len(b)>0:
    x=a.pop(0)
    y=b.pop(0)
    if x>y:
        a.append(y)
        a.append(x)
    elif y>x:
        b.append(x)
        b.append(y)
    cnt+=1
    if a==oa and b==ob:
        print(-1)
        e=False
        break
if e:
    print(cnt,end=' ')
    if len(a)==0:
        print(2)
    else:
        print(1)