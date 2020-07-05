n=int(input())
nums=[]
for i in range(0,n):
    nums.append(input().split())
nums=sorted(nums,key=lambda int(x):int(x[1]),reverse=True)
print(nums[0][0])