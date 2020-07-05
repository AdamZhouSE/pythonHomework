T = int(input())
while T > 0:
    T -= 1
    length = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    sum = int(input())
    isExi = False
    for i in range(0, length - 3):
        for j in range(i, length - 2):
            for k in range(j, length - 1):
                for m in range(k, length):
                    if num[i] + num[j] + num[k] + num[m] == sum:
                        isExi = True
                        break
    if isExi:
        print('1')
    else:
        print('0')
