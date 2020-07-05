T = int(input())
while T > 0:
    T -= 1
    n, v = input().split(' ')
    v = int(v)
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    index = -1
    min = 100
    for i in range(0, len(num)):
        if abs(num[i] - v) <= min:
            min = abs(num[i] - v)
            index = i
    print(num[index])