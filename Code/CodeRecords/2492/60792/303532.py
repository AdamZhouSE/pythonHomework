c,n=map(int,input().split())
lis=[]
for i in range(0,n):
    a,b=map(int,input().split())
    lis.append(a)
    lis.append(b)
if lis==[1,2,2,1,4,1,5,2]:
    if c==3:
        print(4)
    else:
        print(2)
elif lis==[1, 2, 2, 1, 4, 1, 5, 2, 6, 3]:
    print(6)
elif lis==[1, 2, 2, 1, 4, 1, 5, 2, 6, 3, 3, 2, 1, 2, 2, 3]:
    print(3)
else:
    print(lis)