def do(nums:list, P):
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[i] * nums[j] == P:
                print('Yes')
                return
    print('No')


test = int(input())
for t in range(test):
    input1 = input().split(' ')
    N = int(input1[0])
    P = int(input1[1])
    nums = [int(x) for x in input().split(' ')]
    do(nums,P)