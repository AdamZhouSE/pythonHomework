import itertools
import math
import collections
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
nums=[]
lis=list(itertools.combinations([a,b,c,d],2))
for i in range(len(lis)):
    nums.append(math.pow(lis[i][0][0]-lis[i][1][0],2)+math.pow(lis[i][0][1]-lis[i][1][1],2))
dic=collections.Counter(nums)
if len(dic)==2:
    if dic.get(min(nums))==4 and dic.get(max(nums))==2:
        print(True)
    else:
        print(False)
else:
    print(False)