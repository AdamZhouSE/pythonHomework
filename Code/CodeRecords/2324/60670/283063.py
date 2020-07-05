A=sorted(list(map(int,input().split(','))))
k=int(input())
n=len(A)
minn=1000000000
for i in range(0,len):
    A[i]-=k
for i in range(0,len-1):
    A[i]+=(2*k)
    minn=min(minn,max(A)-min(A))
print(minn)