def sumary(nums:list):
    result = 0
    for x in nums:
        result += x
    return result

def do(N,S,nums:list):
    for start in range(N):
        for end in range(i+1,N):
            if sumary(nums[start:end+1]) == S:
                print(start+1,end+1)
                return 
    print(-1)

test = int(input())
for i in range(test):
    input1 = input().split(' ')
    N = int(input1[0])
    S = int(input1[1])
    nums = [int(x) for x in input().split(' ')]
    do(N,S,nums)
