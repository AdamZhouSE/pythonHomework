def lengthOfLIS(nums):

    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        cur_max = 0
        for j in range(i):
            if nums[i] > nums[j]:
                cur_max = max(cur_max, dp[j])
        if cur_max:
            dp[i] = cur_max + 1
    return max(dp)

str = input()

i = 0
lst = []
while i < len(str):
    number = ''
    judge = False
    if str[i]=='-' or (str[i]>='0' and str[i]<='9'):
        judge = True
        number += str[i]
    while judge:
        if i + 1 == len(str):
            lst.append(int(number))
            break
        if str[i + 1] >= '0' and str[i + 1] <= '9':
            i += 1
            number += str[i]
        else:
            judge = False
            lst.append(int(number))
    i += 1
print(lengthOfLIS(lst))