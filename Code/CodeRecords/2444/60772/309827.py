import re


def execute(nums, k, t):
    all_buckets = {}
    bucket_size = t + 1  # 桶的大小设成t+1更加方便
    for i in range(len(nums)):
        bucket_num = nums[i] // bucket_size  # 放入哪个桶

        if bucket_num in all_buckets:  # 桶中已经有元素了
            return "true"

        all_buckets[bucket_num] = nums[i]  # 把nums[i]放入桶中

        if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # 检查前一个桶
            return "true"

        if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # 检查后一个桶
            return "true"

        # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
        if i >= k:
            all_buckets.pop(nums[i - k] // bucket_size)

    return "false"


s = input()
arr = re.findall('\d', s)
t = int(arr.pop())
k = int(arr.pop())
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums, k, t))
