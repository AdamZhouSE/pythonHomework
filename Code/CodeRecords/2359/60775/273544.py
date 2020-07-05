T = int(input())

for t in range(T):
    count = 0
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    for i in range(0,size-2):
        for j in range(i+1,size-1):
            for k in range(j+1,size):
                if nums[i] + nums[j] == nums[k] or nums[i] + nums[k] == nums[j] or nums[j] + nums[k] == nums[i]:
                    count += 1
    if count == 0:
        print(-1)
    else:
        print(count)