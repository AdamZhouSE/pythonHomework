def find_len(nums):
    if len(nums) <= 1:
        return len(nums)
    maxlen = 0
    count = 1
    for i in range(len(nums)-1):
        if nums[i]<nums[i+1]:
            count += 1
        else:
            maxlen = max(count, maxlen)
            count = 1
    maxlen = max(count, maxlen)
    return maxlen


if __name__ == "__main__":
    nums = eval(input())
    print(find_len(nums))