import math
nums=list(map(int,input().split(",")))
g = nums[0]
for i in nums:
    g = math.gcd(g, i)
if g==1:
    print("True")
else:
    print("False")