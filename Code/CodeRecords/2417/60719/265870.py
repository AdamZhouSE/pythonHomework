def gcd(p,q):
    temp = p % q
    while temp != 0:
        p = q
        q = temp
        temp = p % q
    return q


nums = input().split(",")
b = False
d = int(nums[0])
for i in range(1, len(nums)):
    d = gcd(d, int(nums[i]))
if d == 1:
    b = True
print(b)