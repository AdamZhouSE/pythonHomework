times = int(input())
for i in range(times):
    input()
    nums = [int(i) for i in input().split()]
    out = ''
    for j in range(len(nums)):
        if(nums[j]>=max(nums[j:])):
            out=out+str(nums[j])+' '
    print(out[0:-1])