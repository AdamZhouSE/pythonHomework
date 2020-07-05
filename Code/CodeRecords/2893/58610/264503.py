nums = eval(input())
a, b = 0, 0
for num in nums:
    a = a ^ num & ~b
    b = b ^ num & ~a
print(a)