t = int(input())
for h in range(t):
    tem = input().split(' ')
    n = int(tem[0])
    k = int(tem[1])
    tem = input().split(' ')
    nums = []
    for y in tem:
        nums.append(int(y))
    result = -1
    for x in range(n - k + 1):
        tem = 0
        for y in range(k):
            tem = nums[x + y] + tem
        if tem > result:
            result = tem
    print(result)