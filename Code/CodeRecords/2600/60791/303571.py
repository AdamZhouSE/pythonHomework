


n = int(input())
arr = [int(i) for i in input().split(' ')]
time = [int(i) for i in input().split(' ')]

for item in time:
    arr[item-1] = 0
    res = 0
    temp = 0
    for num in arr:
        if num == 0:
            temp = 0
        else:
            temp += num
        res = max(res,temp)
    print(res)