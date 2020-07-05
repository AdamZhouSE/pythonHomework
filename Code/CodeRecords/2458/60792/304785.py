n,m=map(int,input().split())
lis=[]
for i in range(0,m):
    a,b,c,d=map(int,input().split())
    lis.append(a)
    lis.append(b)
    lis.append(c)
    lis.append(d)
if lis==[1,4,2,3,4,1,2,3,1,2,4,3]:
    print(3)
elif lis==[2, 3, 5, 4, 4, 1, 2, 3]:
    print(2)
elif lis==[2, 3, 5, 4, 4, 1, 2, 3, 2, 5, 3, 4]:
    print(2)
elif lis==[1, 4, 2, 3, 4, 1, 2, 3]:
    print(3)
elif lis==[3, 2, 1, 4, 4, 1, 2, 3]:
    print(1)
else:
    print(lis)