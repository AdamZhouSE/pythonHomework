import sys
def gcd(a,b):
    if(b>0):
        return gcd(b,a%b)
    else:
        return a
nums=eval(input())
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if(gcd((int)(nums[i]),(int)(nums[j]))==1):
            print(True)
            sys.exit()
print(False)            
        