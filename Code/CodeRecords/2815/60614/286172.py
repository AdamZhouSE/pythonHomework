length=int(input())
nums=[int(x) for x in input().split()]
now=1
count=0
for i in nums:
    if i>=0:
        count+=abs(i-1)
    else:
        count+=abs(i+1)
        now*=-1
if now>0:
    print(count)
else:
    print(count+2)