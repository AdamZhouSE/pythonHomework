inp = int(input())
nums=input().split(" ")
for i in range(inp):
    nums[i] = int(nums[i])
nums.sort()
res=0
i=1
while(i<=inp-1):
    res = res+(nums[i]-nums[i-1])
    i+=2

print(res)