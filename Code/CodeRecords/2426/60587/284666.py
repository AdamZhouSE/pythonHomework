T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    tmp = 0
    for i in range(0, len(num) - 2):
        for j in range(i + 1, len(num) - 1):
            for k in range(j + 1, len(num)):
                if num[i] * num[j] * num[k] > tmp:
                    tmp = num[i] * num[j] * num[k]
    print(tmp)
