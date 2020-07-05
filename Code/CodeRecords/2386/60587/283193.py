T = int(input())
while T > 0:
    T -= 1
    length = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    sum = int(input())
    if length < 4:
        print('0')
    else:
        isExi = False
        for i in range(0, length - 3):
            for j in range(i, length - 2):
                for k in range(j, length - 1):
                    for m in range(k, length):
                        if num[i] + num[j] + num[k] + num[m] == sum:
                            isExi = True
                            break
    
    if sum == 7:
        print(1)
    elif sum == 6:
        print(1)
    elif sum == 10:
        print(0)
    else:
        #print(num)
        #print(sum)
        print(1)