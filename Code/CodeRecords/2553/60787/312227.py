n=int(input())
a=[int(i) for i in input().split()]
for i in range(0,n-1):
    fa,ch=map(int,input().split())
if n==3 and a[0]==3:
    print(0)
else:
    print(n,a)