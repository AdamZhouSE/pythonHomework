t = int(input())
for i in range(t):
    n = int(input())
    nums = input().split()
    for i in range(n):
        nums[i] = int(nums[i]) % 3
    count_1 = 0
    count_2 = 0
    res = 0
    for j in range(n):
        if nums[j] == 0:
            res += 1
        elif nums[j] == 1:
            count_1 += 1
        elif nums[j] == 2:
            count_2 += 1
    print(int((res + min(count_1, count_2)) + (max(count_1, count_2) - min(count_1, count_2))/3))
    