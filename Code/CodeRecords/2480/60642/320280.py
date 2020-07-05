times = int(input())
for i in range(times):
    input()
    nums = [int(i) for i in input().split()]
    out = []
    for j in range(len(nums)):
        if(nums[j]%2==0):
            out.append(nums[j])
    for j in range(len(nums)):
        if(nums[j]%2==1):
            out.append(nums[j])
    print("".join([str(out[i]) + ' ' for i in range(len(out))])[0:-1])