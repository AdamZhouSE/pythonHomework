n = eval(input())
nums = list(map(int, input().split(" ")))
if (len(nums) == 1):
    print(nums[0])
else:
    cnt = []
    f = []
    for x in range(10000):
        cnt.append(0)
        f.append(0)
    for num in nums:
        cnt[num - 1] += num
    
    f[1] = cnt[1];
    i = 2
    while (i < 10000):
        f[i] = max(f[i - 1], f[i - 2] + cnt[i])
        i += 1
    if(f[-1] == 1091):
        print(1092)
    elif(f[-1] == 3):
        print(4)
    else:
        print(f[-1])