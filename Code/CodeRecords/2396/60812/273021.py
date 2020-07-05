n = int(input())
nums = [int(i) for i in input().split(' ')]
for i in range(n):
    min, index = nums[i], i
    for j in range(i+1, n):
        if nums[j] < min:
            min, index = nums[j], j
    print(index+1, end=' ')
    for j in range(i, (index+i)//2+1):
        nums[j], nums[i+index-j] = nums[i+index-j], nums[j]