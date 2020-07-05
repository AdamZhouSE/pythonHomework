import math
def fuc(n):
    result=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            result=result*i
    return result
n=int(input())
count=0
for i in range(2,n+1):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        count+=1
print(((fuc(count)*fuc(n-count))%(((10**9))+7)))
