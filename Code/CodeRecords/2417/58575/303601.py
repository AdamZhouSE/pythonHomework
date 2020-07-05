def gcd(a,b):
    if b==0:
        return a
    return gcd(min(a,b),max(a,b)%min(a,b))


nums=list(map(int,input().split(",")))
GcdNum=nums[0]
i=1
while i<len(nums):
    GcdNum=gcd(GcdNum,nums[i])
    i+=1
if GcdNum==1:
    print(True)
else:
    print(False)