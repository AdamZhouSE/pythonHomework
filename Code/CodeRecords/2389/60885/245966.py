def test():
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(0, len(nums), 2):
        if i <= len(nums)-2:
            nums[i],nums[i+1] = nums[i+1],nums[i]
    result.append(' '.join(list(map(str, nums))))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)