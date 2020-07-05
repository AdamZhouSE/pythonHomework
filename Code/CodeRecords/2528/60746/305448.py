N=list(input())
nums=[]
nn=len(N)
for i in range(nn):
    k=N[i]
    if k.isdecimal():
        nums.append(int(k))
nnums=len(nums)
for i in range(nnums):
    nums[i]=int(nums[i])
def Ascend(A:list):
    n=len(A)
    for i in range(0,n):
        for p in range(i+1,n):
            if A[i]>A[p]:
                t=A[i]
                A[i]=A[p]
                A[p]=t
    print(A)
    return 0
Ascend(nums)