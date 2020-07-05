def C(nums:list,k):
    if k == 0:
        return [[]]
    result = []
    for i in range(len(nums)):
        tmp = [nums[i]]
        for x in C(nums[i+1:], k-1):
            result.append(tmp + x)
    return result

test = int(input())
for i in range(test):
    num = int(input())
    ability = [int(x) for x in input().split(' ')]
    max_ability = -1 * pow(2,31)
    for x in C(ability,3):
        if x[0] * x[1] * x[2] > max_ability:
            max_ability = x[0] * x[1] * x[2]
    print(max_ability)