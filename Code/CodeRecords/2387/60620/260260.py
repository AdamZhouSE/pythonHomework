n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    op,l,r=map(int,input().split())
    if(op==0):
        a[(l-1):r]=sorted(a[(l-1):r])
    if(op==1):
        a[(l-1):r]=sorted(a[(l-1):r],reverse=True)
q=int(input())
print(a[q-1])
