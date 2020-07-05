times = int(input())
for j in range(times):
    input()
    nums = [int(i) for i in input().split()]
    strg = ''
    for i in range(len(nums)):
        if(i==len(nums)-1 or nums[i]<=nums[i+1]):
            strg+='-1 '
        else:
            strg+=str(nums[i+1])+' '
    print(strg)