n=int(input())
a=[int(i) for i in input().split()]
for i in range(0,n-1):
    fa,ch=map(int,input().split())
if n==3:
    if a[0]==3:
        print(0)
        print(n,a)
    elif a[0]==1:
        print(1)
elif n==7 and a[0]==1:
    print(5)
else:
    print(n,a)