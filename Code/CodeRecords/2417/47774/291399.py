nums=list(eval(input()))
def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
    
g = nums[0]
for num in nums:
    g = gcd(g, num)
print(g == 1)
