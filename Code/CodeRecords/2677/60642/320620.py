times = int(input())
for i in range(times):
    input()
    nums = [int(i) for i in input().split()]
    temp = []
    out = 0
    for j in range(len(nums)):
        if(temp.count(nums[j])==0 and nums.count(nums[j])!=0):
            temp.append(nums[j])
            out+=sum([i for i in range(nums.count(nums[j]))])
    print(out)