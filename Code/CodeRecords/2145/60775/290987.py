
T = int(input())
for t in range(T):
    n = int(input())
    nums = [int(x) for x in input().split(' ')]
    max_area = 0
    for start in range(n):
        max1 = nums[start]
        min1 = nums[start]
        for end in range(start,n):
            max1 = max(max1,nums[end])
            min1 = min(min1,nums[end])
            tmp_max = max(max1,min1*(end-start+1))
            max_area = max(max_area,tmp_max)
    print(max_area)