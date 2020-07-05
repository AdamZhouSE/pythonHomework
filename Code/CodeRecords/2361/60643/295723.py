import math
def numSquarefulPerms(lst):
    nums = lst
    nums.sort()
    res = []

    def backtrack(nums, tmp):
        if not nums:#如果nums为空
            res.append(tmp)
            return
        for i in range(len(nums)):
            # 去重
            if i>=1 and nums[i] == nums[i - 1]:
                continue
            # 剪枝
            if not tmp or math.sqrt(tmp[-1] + nums[i]) % 1 == 0:#temp为空 或者 tmp[-1]+nums[i]是一个完全平方数
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])#回溯 nums除去nums[i]以外的元素， 同时将nums[i]加到tmp中去

    backtrack(nums, [])
    return len(res)

if __name__=="__main__":
    a=input().split(",")
    a=[int(x) for x in a]
    res=numSquarefulPerms(a)
    print(res)