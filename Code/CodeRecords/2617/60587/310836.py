T = int(input())
while T > 0:
    T -= 1
    nums, tar = input().split(' ')
    tar = int(tar)
    res = 0
    for i in range(len(nums) + 1):
        for j in range(i + 1, len(nums) + 1):
            tmp = nums[i:j]
            # print(tmp)
            count = 0
            for k in range(len(tmp)):
                if tmp[k] == '1':
                    count += 1
            if count == tar:
                res += 1
    print(res)
