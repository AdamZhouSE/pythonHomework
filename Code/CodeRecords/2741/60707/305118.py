
def findLengthOfLCIS(nums):
    if not nums:        
        return 0

    res = 1                             # 初始化结果变量
    cur_len = 1                         # 初始化当前连续递增长度
    for i in range(1, len(nums)):       # 遍历
        if nums[i-1] < nums[i]:         # 如果发现递增对
            cur_len += 1                # 长度+1
            res = max(cur_len, res)     # 更新结果
        else:                           # 遇到非递增对
            cur_len = 1                 # 重置当前连续递增长度
    return res

if __name__ == '__main__':
    inp1 = input().split("[")
    temp1 = inp1[1].split("]")
    temp2 = temp1[0].split(",")
    nums = [int(x) for x in temp2]

    res = findLengthOfLCIS(nums)

    print(res)
