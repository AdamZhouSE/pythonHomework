
T = int(input())

for t in range(T):
    input1 = input().split(' ')
    size = int(input1[0])
    K = int(input1[1])
    nums = [int(x) for x in input().split(' ')]

    for i in range(0,size,K):
        if size - i < K:
            tmp = nums[i:]
            tmp.reverse()
            nums[i:] = tmp
        else:
            tmp = nums[i:i+K]
            tmp.reverse()
            nums[i:i+K] = tmp

    for i in range(size):
        print(str(nums[i]) + ' ',end='')
    print()