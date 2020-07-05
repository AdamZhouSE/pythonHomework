n=int(input())
a=list(map(int,input().split()))
b=[i for i in range(n)]
for i in range(n):
    b[a[i]-1]=i+1
for i in range(n-1):
    print(b[i],end=" ")
print(b[-1])