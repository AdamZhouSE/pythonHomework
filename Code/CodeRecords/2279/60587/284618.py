T = int(input())
while T > 0:
    T -= 1
    n, sum = input().split(' ')
    sum = int(sum)
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    res = ''
    start = 0
    while True:
        tmp = 0
        isFind = False
        for i in range(start, len(num)):
            if tmp < sum:
                tmp += num[i]
            elif tmp > sum:
                break
            else:
                res = res + str(start + 1) + ' ' + str(i)
                isFind = True
                break
        if isFind:
            break
        else:
            start += 1
    print(res)