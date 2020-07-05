T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    num.sort()
    res = 0
    for i in range(0, n - 2):
        for j in range(i+1, n - 1):
            for k in range(j+1, n):
                if num[i] + num[j] == num[k]:
                    res += 1
    if res == 0:
        print('-1')
    else: 
        print(res)
    # print(num)
