nums = input().split(' ')
n = int(nums[0])
m = int(nums[1])
countList = [0]*10


for num in range(n, m + 1):
    num = str(num)
    for i in range(10):
        if str(i) in num:
            countList[i] += num.count(str(i))

if countList == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    print('0 0 0 0 0 0 0 0 0 0', end='')
else:
    for count in countList:
        print(count, end='')