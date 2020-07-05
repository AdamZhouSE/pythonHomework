def get_least_numbers(arr, k):
    nums = [0] * 10000  # 申请一个包含最大值个数的元素
    for a in arr:
        nums[a] += 1  # 对重复元素计数
    output = []
    i = 0  # 从0开始遍历（从最小值开始遍历）
    while len(output) < k:
        if nums[i] >= 1:  # 如果该索引处的值大于1，则说明该值存在至少1次，循环往output里面写
            for j in range(nums[i]):
                output.append(i)
        i += 1
    return output[:k]  # 一定要注意单个重复的元素多余k个的情况



print(input())