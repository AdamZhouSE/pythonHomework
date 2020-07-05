def cut(s: str):
    results = []
    num = 0
    for x in range(len(s)):
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results

def selfMul(x):
    res = 1
    while x > 0:
        temp = x % 10
        res *= temp
        x //= 10
    return res

T = int(input())
while T>0:
    T -= 1
    str = input()
    lst = cut(str)
    nums = [int(x) for x in lst]
    length = len(nums)
    mul = [0] * length
    condition = 1
    for i in range(length):
        temp = selfMul(nums[i])
        if temp not in mul:
            mul.append(temp)
        else:
            condition = 0
    print(condition)
