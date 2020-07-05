n, p = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
ms = int(input())
for m in range(ms):
    formula = input()
    if formula.startswith('1'):
        t, g, c = map(int, formula[2:].split(' '))
        nums[t - 1:g] = map(lambda x: x * c, nums[t - 1:g])
    elif formula.startswith('2'):
        t, g, c = map(int, formula[2:].split(' '))
        nums[t - 1:g] = map(lambda x: x + c, nums[t - 1:g])
    else:
        t, g = map(int, formula[2:].split(' '))
        print((sum(nums[t - 1:g])) % p)
