nums = [int(i) for i in input().split(',')]
n = len(nums)
start, end, middle = 0, n, n//2
h = 0
while start != end:
    if nums[middle] == n-middle or nums[middle] == n-middle-1:
        h = nums[middle]
        break
    elif nums[middle] < n-middle-1:
          start = middle+1
    else:
        end = middle
    middle = (end+start)//2
print(h)