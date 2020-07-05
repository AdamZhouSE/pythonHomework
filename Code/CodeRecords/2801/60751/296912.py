n=int(input())
nums=list(map(int,input().split(" ")))
nums.sort()
a=0
for i in range(len(nums)-2):
    if nums[i]+nums[i+1]>nums[i+2]:
        a=1
        break
if a==1:
    print("YES")
else:
    print("NO")
