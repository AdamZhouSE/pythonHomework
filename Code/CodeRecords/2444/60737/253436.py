def contain_d(nums, k, t):
    if k < 0 or t < 0:
        return 'false'
    Bucket = {}
    Bucket_size = t + 1
    for i in range(len(nums)):
        bucket_number = nums[i] // Bucket_size
        if bucket_number in Bucket:
            return 'true'
        Bucket[bucket_number] = nums[i]
        if bucket_number - 1 in Bucket and nums[i] - Bucket[bucket_number - 1] <= t:
            return 'true'
        if bucket_number + 1 in Bucket and Bucket[bucket_number + 1] - nums[i] <= t:
            return 'true'
        if i >= k:
            Bucket.pop(nums[i-k] // Bucket_size)
    return 'false'


if __name__ == "__main__":
    cmd = input().replace('nums = ', '').replace(', k = ', ' ').replace(', t = ', ' ').split(' ')
    nums=eval(cmd[0])
    k=int(cmd[1])
    t=int(cmd[2])
    print(contain_d(nums, k, t))
    