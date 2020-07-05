from itertools import combinations
import numpy as np
from itertools import combinations
def num(k,n):
    nums=[1,2,3,4,5,6,7,8,9]
    res=[]
    for i in range(len(nums)):
        res +=list(combinations(nums,i))
    res=[x for x in res if len(x) == k]
    a=[]
    for j in res:
        if sum(j) ==n :
            a.append(list(j))
    return a


inp = input().split(',')
k = int(inp[0])
n = int(inp[1])
print(num(k,n))
'''
print("k: ",k)
print("n: ",n)
nums = [1,2,3,4,5,6,7,8,9]
res = []
for i in range(9):
    res += list(combinations(nums,k))

result = []
for j in res:
    if(sum(j) == n):
        result.append(list(j))
print(np.unique(result))
print(result)'''