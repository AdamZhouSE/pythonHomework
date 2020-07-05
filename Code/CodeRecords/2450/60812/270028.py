nums = [int(i) for i in input().split(',')]
target = int(input())
n = len(nums)
start, end = 0, n
while start != end:
    middle = (start+end)//2
    temp = nums[middle]
    if temp < target:
        start = middle+1
    elif temp > target:
        end = middle
    else:
        for i in range(middle, n):
            if nums[i] == target:
                end = i
        for i in range(middle, -1, -1):
            if nums[i] == target:
                start = i
        print('[{}, {}]'.format(start, end))
        break
else:
    print('[-1, -1]')