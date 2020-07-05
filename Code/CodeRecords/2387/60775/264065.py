all = input().split(' ')
length = int(all[0])
times = int(all[1])
nums = [int(x) for x in input().split(' ')]

for i in range(times):
    parameter = [int(x) for x in input().split(' ')]
    mode = parameter[0]
    start = parameter[1]
    end = parameter[2]
    tmp = nums[start-1:end]
    if mode == 1:
        tmp.sort(reverse=True)
    else:
        tmp.sort()
    nums[start-1:end] = tmp
print(nums[int(input())-1])
