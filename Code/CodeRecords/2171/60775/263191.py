def do(size,nums:list):
    idx_even = 0
    result = []
    for x in nums:
        if x % 2 == 0:
            result.insert(idx_even,x)
            idx_even += 1
        else:
            result.append(x)
    return result

test = int(input())
for i in range(test):
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    result = do(size , nums)
    for x in result:
        print(str(x)+' ',end= '')
    print()