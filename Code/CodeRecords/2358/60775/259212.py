num_of_test = int(input())
for i in range(num_of_test):
    input1 = input().split(' ')
    large = int(input1[0])
    rank = int(input1[1])
    nums = [int(x) for x in input().split(' ')]
    for j in range(rank):
        for k in range(len(nums)-1,j,-1):
            if nums[k] > nums[k-1]:
                tmp = nums[k]
                nums[k] = nums[k-1]
                nums[k-1] = tmp
    result = [str(x) for x in nums[0:rank]]
    print(' '.join(result)+' ')
    

