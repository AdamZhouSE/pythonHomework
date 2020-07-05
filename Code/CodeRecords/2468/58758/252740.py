count = int(input())
ans = []
for i in range(0, count):
    n = int(input())
    nums = [int(x) for x in input().split()]
    mults = []
    for j in range(0, len(nums)):
        mult = 1
        for k in range(0, len(nums)):
            if k == j:
                pass
            else:
                mult *= nums[k]
        mults.append(mult)
    ans.append(mults)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
