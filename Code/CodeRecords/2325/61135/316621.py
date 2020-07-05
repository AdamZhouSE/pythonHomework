nums=input().split(",")
nums=list(int(a) for a in nums)
from collections import Counter
nums=Counter(nums)
sign=1
for i in range(2, 10001):
    count = 0
    for c in nums.values():
        if c%i==0: 
            count=count+1
        else:
            break
    if(count==len(nums)):
        print(True)
        sign=0
if(sign==1):
    print(False)