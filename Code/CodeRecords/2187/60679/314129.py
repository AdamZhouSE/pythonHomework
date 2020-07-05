T = int(input())
result = []
for i in range(T):
    read = input()
    N = int(read[0:read.index(' ')])
    K = int(read[read.index(' '):len(read)])
    read = input()
    nums = read.split(' ')
    nums = [int(nums[i]) for i in range(len(nums))]
    largest = 0
    for j in range(N-K+1):
        sum = 0
        for k in range(K):
            sum = sum + nums[j+k]
        if(sum>largest):
            largest = sum
    result.append(largest)
for i in range(T):
    print(result[i])