n=int(input())
nums=[]
for i in range(0,n):
    nums.append(input().split())
nums=sorted(nums,key=lambda x:int(x[1]),reverse=True)
print(nums)