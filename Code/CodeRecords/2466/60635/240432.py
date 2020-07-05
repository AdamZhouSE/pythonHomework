count = int(input())
for i in range(count):
    ans = 0
    l = int(input())
    nums = [int(x) for x in input().split()]
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j]+nums[k] > nums[i]:
                    ans+=1
    print(ans)
