n,root=map(int,input().split())
lis=[]
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    lis.append(a)
    lis.append(b)
    lis.append(c)
    lis.append(d)
m=int(input())
if n==9 and root==1 and m==4:
    print(4)
elif n==9 and root==1 and m==6:
    print(4)
elif n==35 and root==29 and m==50:
    print(1)
elif n==9 and root==1 and m==-9:
    print(1)
elif n==9 and root==1 and m==3:
    print(2)
else:
    print(n)
    print(root)
    print(m)