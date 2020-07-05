def check(maxSum):
    tempSum=0
    count=0
    for num in nums:
        if num>maxSum:      # 如果单个数字大于maxSum，直接根本就无法分割出和小于maxSum的一组
            return False
        if (tempSum+num)>maxSum:   # 如果和超过了maxSum，另起一组
            count+=1
            tempSum=num
        else:     # 贪心策略，一组中放的数字尽可能多
            tempSum+=num
    return (count+1)<=maxCount    # 分割完成后 sum里还有一组

if __name__ == '__main__':
    import math
    nums=list(map(int,input().split(",")))
    maxCount=eval(input())
    left=1
    right=1
    for i in range(len(nums)):
        right+=nums[i]
    result=-1
    while left<right:
        mid=math.floor((left+right)/2)
        if check(mid):
            result=mid
            right=mid
        else:
            left=mid+1
    print(result)
