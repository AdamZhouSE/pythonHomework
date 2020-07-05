import sys
s=[int(x) for x in input().split(',')]
low=0
high=len(s)-1
if s[1]>s[0] and s[1]>s[2]:
    print(1)
    sys.exit(0)
while low<high:
    mid1=int((low+high)/2)
    mid2=mid1+1
    if s[mid1]<s[mid2]:
        low=mid2
    else:
        high=mid1
print(low)