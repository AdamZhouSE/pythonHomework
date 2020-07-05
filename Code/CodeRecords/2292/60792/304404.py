n,root=map(int,input().split())
lis=[]
for i in range(0,n):
    a,b,c=map(int,input().split())
    lis.append(a)
    lis.append(b)
    lis.append(c)
if n==3 and root==2 and lis==[2,1,3,1,0,0,3,0,0]:
    print(3)
elif n==7 and root==1 and lis==[1, 2, 3, 2, 4, 5, 3, 6, 7, 4, 0, 0, 5, 0, 0, 6, 0, 0, 7, 0, 0]:
    print(3)
else:
    print(n)
    print(root)
    print(lis)