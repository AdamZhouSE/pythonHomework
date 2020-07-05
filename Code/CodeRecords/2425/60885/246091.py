def test():
    N,K = list(map(int, input().split()))
    nums = sorted(list(map(int, input().split())) + [K])
    i = nums.index(K)
    if i == 0:
        result.append(nums[1])
    elif i == len(nums)-1:
        result.append(nums[-2])
    else:
        a,b = nums[i-1], nums[i+1]
        da,db = K-a, b-K
        if da >= db:
            result.append(b)
        else:
            result.append(a)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)