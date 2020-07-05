A=sorted(list(map(int,input().split(','))))
k=int(input())
n=len(A)
minn=max(A)-min(A)
for i in range(0,n):
    A[i]-=k
for i in range(0,n-1):
    A[i]+=(2*k)
    minn=min(minn,max(A)-min(A))
print(minn)