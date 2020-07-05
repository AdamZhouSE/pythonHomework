nums = [int(i) for i in input().split(',')]
target = int(input())
n = len(nums)
start, end, index = 0, n, 0
while start != end:
    middle = (start+end)//2
    temp = nums[middle]
    if temp < target:
        start = middle+1
    elif temp > target:
        end = middle
    else:
        index = middle
        break
else:
    index = start
for i in range(index-1):
    for j in range(i+1, index):
        if nums[i]+nums[j] == target:
            print('[{}, {}]'.format(i+1, j+1))
            break
    else:
        continue
    break
else:
    print('None')