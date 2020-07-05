def test():
    N,P = list(map(int, input().split()))
    nums = sorted(list(map(int, input().split())))
    l,r = 0,len(nums)-1
    while l < r:
        ans = nums[l] * nums[r]
        if ans == P:
            result.append('Yes')
            break
        elif ans > P:
            r -= 1
        else:
            l += 1
    else:
        result.append('No')

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)