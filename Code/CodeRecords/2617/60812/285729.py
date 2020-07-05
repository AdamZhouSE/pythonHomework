T = int(input())
for i in range(T):
    s, k = input().split(' ')
    k = int(k)
    nums = [0 for i in range(k+1)]
    length = k+1
    num = 0
    for i in s:
        if i == '0':
            nums[num] += 1
        else:
            num += 1
            if num == length:
                nums.append(0)
                length += 1
    start, sum, end = 0, 0, k
    while end != length:
        sum += 1+nums[start]+nums[end]+nums[start]*nums[end]
        start += 1
        end += 1
    print(sum)