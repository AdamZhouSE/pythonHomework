import math
t=int(input())
while t:
    nums=[int(x) for x in input().split()]
    i=nums[0]
    L=nums[1]
    print(pow(2,L)-i)
    t-=1