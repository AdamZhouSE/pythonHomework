def average(nums):
    return sum(nums)/len(nums)

def d(nums):
    ave = average(nums)
    result = 0
    for num in nums:
        result += pow(ave - num,2)
    return result/len(nums)

N,M = list(map(int,input().split(" ")))
nums = list(map(int,input().split(" ")))
while(M != 0):
    M = M - 1
    op = list(map(int,input().split(" ")))
    if(op[0] == 1):
        for x in range(op[1] - 1,op[2]):
            nums[x] += op[3]
    elif(op[0] == 2):
        print("%.4f" %(average(nums[op[1] - 1:op[2]])))
    else:
        print("%.4f" %(d(nums[op[1] - 1:op[2]])))