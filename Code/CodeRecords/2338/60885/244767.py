def test():
    N,X = list(map(int, input().split()))
    nums = sorted(list(map(int, input().split())))

    l, r = 0, len(nums)-1
    while l < r:
        sum = nums[l] + nums[r]
        if sum == X:
            result.append('Yes')
            break
        elif sum < X:
            l += 1
        else:
            r -= 1
    else:
        result.append('No')

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)