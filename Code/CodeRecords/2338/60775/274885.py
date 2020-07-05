def print_list(nums:list):
    #打印数组
    for i in range(len(nums)):
        print(str(nums[i]) + ' ',end='')
    print()


def do(nums: list, size, X):
    for i in range(size-1):
        for j in range(i+1,size):
            if nums[i] + nums[j] == X :
                return 'Yes'
    return 'No'


T = int(input())
for t in range(T):
    input1 = input().split(' ')
    size = int(input1[0])
    X = int(input1[1])
    nums = [int(x) for x in input().split(' ')]
    print(do(nums,size,X))






