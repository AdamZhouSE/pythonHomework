def gcd(a,b):
    return gcd(b,a%b)if a%b else b
nums=list(map(int,input().split(',')))
x=nums[0]
n=len(nums)
for i in range(1,n):
    if(nums[i]):
        x=gcd(x,nums[i])
print(x==1)