n=int(input())
num=input().split(" ")
nums=list(int(a) for a in num)
nums=sorted(nums)
for i in range(0,n-1):
    print(nums[i],end=" ")
print(nums[n-1])