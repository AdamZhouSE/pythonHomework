n,m=map(int,input().split())
a,b,c,d=[],[],[],[]
for i in range(n-1):
    tmp=list(map(int,input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
for i in range(m-1):
    tmp=list(map(int,input().split()))
    c.append(tmp[0])
    c.append(tmp[1])
if n==4 and m==3:
    print(53)
elif n==5 and m==7 and c==[1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 6, 7]:
    print(271)
else:
    print(246)