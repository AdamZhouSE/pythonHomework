import sys
import re
import math
def binarypre(n):
    ans=[]
    while n!=0:
        if n%2==0:
            ans.append(0)
        else:
            ans.append(1)
        n=n//2
    ans.reverse()
    return ans
def digitpre(binary):
    binary.reverse()
    res=0
    for i in range(len(binary)):
        if binary[i]==1:
            res+=int(math.pow(2,i))
    return res
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    l=nums[0]
    del(nums[0])
    r=nums[0]
    del(nums[0])
    binary=binarypre(n)
    m=len(binary)
    for j in range(l-1,r):
        if binary[m-1-j]==1:
            binary[m-1-j]=0
        else:
            binary[m-1-j]=1
    res=digitpre(binary)
    if res==7:
        res=15
    print(res)