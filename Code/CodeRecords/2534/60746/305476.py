A=list(input())
nn=len(A)
N=[]
for i in range(nn):
    if A[i].isdecimal():
        N.append(int(A[i]))
def Ascend(nums:list)->list:
    n=len(nums)
    for i in range(0,n):
        for p in range(i+1,n):
            if nums[i]>nums[p]:
                t=nums[i]
                nums[i]=nums[p]
                nums[p]=t
    return nums
print(Ascend(N))
