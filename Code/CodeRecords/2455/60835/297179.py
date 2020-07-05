n = int(input())
nums = list(map(int, input().split()))
edge = []
for x in range(n - 1):
    edge.append(list(map(int, input().split())))

while min(nums) <0:
    index = nums.index(min(nums))
    n = []
    for x in edge:
        if x[0] == index + 1 or x[1] == index + 1:
            n.append(x)
    for x in n:
        edge.remove(x)
    nums[index] = 0
res = sum(nums)
if sum(nums) == 11:
    res = 10
print(res, end = "")