def length_of_lis(nums):
    len_nums = len(nums)
    if len_nums == 0:
        return 0

    dp = [1] * len_nums
    for i in range(len_nums - 1):
        for j in range(i + 1):
            # 如果nums[i+1]能缀在nums[j]后面的话，就dp[j]+1
            if nums[i + 1] > nums[j]:
                # 缀完的结果还要看看是不是比我大
                dp[i + 1] = max(dp[i + 1], dp[j] + 1)
    return max(dp)
t = int(input())
for i in range(t):
    tmp = input()
    tmp = input()
    arr = [int(k) for k in tmp.split(" ") ]
    print(length_of_lis(arr)-1)