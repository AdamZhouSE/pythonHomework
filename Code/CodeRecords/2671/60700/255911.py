def A(x, y):
    a = 1
    for i in range(x-y+1, x+1):
        a *= i
    return a


def C(x, y):
    return A(x, y)//A(y, y)


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in nums:
    n = int(i)
    invalidNum = 0
    for j in range((n+1)//2+1):
        invalidNum += C(n-j+1, j)
    print(2**n - invalidNum)
