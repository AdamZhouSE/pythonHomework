T = int(input())
while T > 0:
    T -= 1
    length, n = input().split(' ')
    length = int(length)
    n = int(n)
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    lst = list(num)
    lst.sort()
    lst.reverse()
    res = ''
    for j in range(n):
        res = res + ' ' + lst[j]
    print(res.lstrip())
