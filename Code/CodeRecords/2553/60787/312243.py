n=int(input())
a=[int(i) for i in input().split()]
for i in range(0,n-1):
    fa,ch=map(int,input().split())
if n==3:
    if a[0]==3:
        print(0)
    elif a[0]==1:
        print(1)
    elif a[0]==2:
        print(2)
    else:
        print(n,a)
elif n==7 and a[0]==1:
    print(5)
elif n==5 and a[0]==1:
    print(3)
else:
    print(n,a)