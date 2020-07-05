nums = [int(i) for i in input().split(',')]
target = int(input())
n = len(nums)
start, end, temp = 0, n, 0
while start != end:
    middle = (start+end)//2
    temp = nums[middle]
    if temp < target:
        start = middle+1
    elif temp > target:
        end = middle
    else:
        print(middle)
        break
else:
    print(start)
