def test():
    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
    result.append(count)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)