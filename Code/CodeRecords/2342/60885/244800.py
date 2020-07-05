def test():
    N,K = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for i in range(0,N,K):
        if i+K >= len(nums):
            nums = nums[:i] + nums[i:][::-1]
        else:
            nums = nums[:i] + nums[i:i+K][::-1] + nums[i+K:]
    result.append(nums)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(' '.join(list(map(str, i))), end=' \n')