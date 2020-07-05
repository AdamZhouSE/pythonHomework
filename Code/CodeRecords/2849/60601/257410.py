def solve(nums:list):
    re = -1
    for i in nums:
        isOK = True
        for j in nums:
            if j%i!=0:
                isOK = False
                break
        if isOK:
            re = i
            break
    return re
    pass

n = eval(input())
nums = list(map(int,input().split(' ')))
print(solve(nums))
