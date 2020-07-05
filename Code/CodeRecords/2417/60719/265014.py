def gcd(p,q):
    temp = p % q
    while temp != 0:
        p = q
        q = temp
        temp = p % q
    return q


nums = input().split(",")
b = False
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if gcd(int(nums[i]), int(nums[j])) != 1:
            b = True
print(b)