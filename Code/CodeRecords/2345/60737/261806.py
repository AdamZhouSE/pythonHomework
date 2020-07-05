t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    nums.sort()
    a, b = 0, 0
    for i in range(l-1):
        if nums[i+1] == nums[i]:
            a = nums[i]
            break
    newnum = [0]*l
    for j in range(l):
        newnum[j] = j+1
    ret = list(set(newnum) ^ set(nums))
    print('{0} {1}'.format(a,ret[0] if ret else 0))
    t -= 1
    