nums = input().split(' ')
n = int(nums[0])
m = int(nums[1])
countList = [0]*10

if n == m:
    pass
else:
    for num in range(n, m + 1):
        if num == 0:
            continue
        num = str(num)
        for i in range(10):
            if str(i) in num:
                countList[i] += num.count(str(i))

for i in range(len(countList)):
    if i != len(countList) - 1:
        print(countList[i], end=' ')
    else:
        print(countList[i], end='')