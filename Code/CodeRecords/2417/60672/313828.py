import sys
def gcd(n,m):
    if n%m==0:
        return m
    elif m%n==0:
        return n
    else:
        p=min(m,n)
        q=max(m,n)%p
        return gcd(p,q)
        
nums=list(input())
indicate=False
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if gcd(nums[i],nums[j])==1:
            indicate=True
            print(indicate)
            sys.exit()
print(indicate)