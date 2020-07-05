nums=list(map(int,input().strip().split(",")))
target=int(input())
if target not in nums:
    print("[-1, -1]")
else:
    print(+str([i for i,x in enumerate(nums) if x==target])+", "+str([i for i,x in enumerate(nums) if x==target]))