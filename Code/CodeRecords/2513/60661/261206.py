n=int(input())
nums=[]
for i in range(n):
    temp=eval(input())
    nums.extend(temp)
k=eval(input())
nums.sort()
print(nums[k-1])