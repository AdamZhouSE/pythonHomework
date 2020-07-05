def length_of_lis(nums):
    # tails[i] 表示长度为i+1的最长上升子序列的末尾值
    # 每次遍历使用二分查找进行更新
    tails, res = [0] * len(nums), 0
    for num in nums:
        i, j = 0, res
        while i < j:
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
            else:
                j = m
        tails[i] = num
        if j == res:
            res += 1
    return res


if __name__ == '__main__':
    print(length_of_lis(eval(input())))