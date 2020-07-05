def gcd(a, b):
    if(b == 0):
        return a;
    return  gcd(b, a%b)

nums = input().split(",")
d = int(nums[0])
for x in range(1, len(nums)):
    d = gcd(d, int(nums[x]))
if d == 1:
    print("True")
else:
    print("False")
