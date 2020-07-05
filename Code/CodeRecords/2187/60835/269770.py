t = int(input())
for x in range(t):
    tem = input().split(' ')
    n = int(tem[0])
    k = int(tem[1])
    tem = input().split(' ')
    nums = []
    for y in tem:
        nums.append(int(y))
    nums.sort()
    result = 0
    for y in range(k):
        result = result + nums[len(nums)-y-1]
    print(result)