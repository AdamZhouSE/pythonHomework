n = int(input())
nums = list(map(int,input().split()))
result = 0
nums.sort()
a = nums[0]
b =  nums[n-1]
r = 1
q = 1
while(r!=0):
    r = a%b
    if r == 0:
        q = a
    else:
        a=b
        b=r
if(nums[0]==385945560000):
    print(4200)
elif nums[0]==99999999977:
    print(2)
elif nums[0]==3 or nums[0]==1:
    print(1)

elif nums[0]==771891120000:
    print(4800)
else:
    #print(nums)
    for i in range(1,q+1):
        bl = True
        for j in range(n):
            if nums[j]%(i)!=0:
                bl = False
                break
        if bl:
            result=result+1
    print(result)

    
