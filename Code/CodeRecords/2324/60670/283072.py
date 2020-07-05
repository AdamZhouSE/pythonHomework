A=sorted(list(map(int,input().split(','))))
k=int(input())
n=len(A)
minn=99999999
for i in range(0,n):
    A[i]-=k
for i in range(0,n-1):
    A[i]+=(2*k)
    minn=min(minn,max(A)-min(A))
if n==1:
    print(0)
else:
    print(minn)