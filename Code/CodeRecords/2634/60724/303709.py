A=eval(input())
k=int(input())
nums=[]
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        num=[A[i],A[j]]
        nums.append(num)
for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j][0]*nums[j+1][1]>nums[j][1]*nums[j+1][0]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums[k-1])