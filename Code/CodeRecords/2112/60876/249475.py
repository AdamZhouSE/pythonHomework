nums=list(map(int,input().split(",")))
max=len(nums)
for i in range(0,max+1):
    if not i in nums:
        print(i)
        break