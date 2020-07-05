n=int(input())
nums=[]
for i in range(n):
    l=input().split(",")
    for e in l: nums.append(int(e))
k=int(input())
nums.sort()
print(nums[k-1])