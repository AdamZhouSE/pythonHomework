def test():
    N = int(input())
    nums = input().split()
    d = int(input())
    nums = nums[d:] + nums[:d]
    result.append(nums)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(' '.join(i), end=' \n')