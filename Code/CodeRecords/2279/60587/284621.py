T = int(input())
while T > 0:
    T -= 1
    n, sum = input().split(' ')
    sum = int(sum)
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    res = ''
    start = 0
    isFind = False
    while True:
        tmp = 0
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
            print(res)
            break
        else:
            start += 1
    if not isFind:
        print('-1')
