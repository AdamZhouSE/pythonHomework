import math
a = int(input())

def helper(n):
    res = list()
    while n > 0:
        res.append(pow(n % 10, 2))
        n = int(n/10)
    return sum(res)

left = a
right = a
left = helper(left)
right = helper(right)
right = helper(right)
while left != right:
    left = helper(left)
    right = helper(right)
    right = helper(right)
print(left == 1)

