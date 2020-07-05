'''第一组线性表第17题
题目描述不清楚
根据原网站的搜索结果和实际测试，感觉题目说的应该是包含k个1的子字符串的数量
（图片传不上去，题目就一行，挺明显的）'''

def do(nums:list, k:int):
    minlen = int(pow(2, 31))
    if nums[-1] >= k:
        return 1
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            tmp = nums[i:j+1]
            sum1 = 0
            for z in tmp:
                sum1 += z
            if sum1 >= k and len(tmp) < minlen:
                minlen = len(tmp)
    return minlen

k = int(input())
nums = [int(x) for x in input().split(',')]
print(do(nums,k))









