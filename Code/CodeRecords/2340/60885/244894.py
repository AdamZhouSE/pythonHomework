def test():
    N = int(input())
    nums = list(map(int, input().split()))
    load = 0
    while len(nums) > 1:
        if nums[0] > nums[-1]:
            nums = nums[::-1]
        h = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < h:
                load += h - nums[i]
            else:
                nums = nums[i:]
                break
    result.append(load)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)