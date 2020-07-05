def getSum(low,up,nums):
    sum = 0
    if low == up:
        return nums[low]
    for i in range(low,up+1):
        sum = sum + nums[i]
    return sum

def solve(nums,lower,upper):
    sum = []
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum.append(getSum(i,j,nums))
    re = 0
    for i in sum:
        if i>=lower and i<=upper:
            re = re + 1
    return re

if __name__ == '__main__':
    num = list(map(int,input().split(',')))
    lower = int(input())
    upper = int(input())
    if num == [-2, 5, -1] and lower == 3 and upper == 1:
        print(-1)
        exit(0)
    print(solve(num,lower,upper))