import math
import itertools
res=input().split(',')
maxsize=input()
leng=len(maxsize)
reslen=len(res)
ans=0
tmp=math.factorial(reslen)
for i in range(1,leng):
    ans+=reslen**i
for array in itertools.product(res,repeat=leng):
    num=int("".join(array))
    if(num<=int(maxsize)):
        ans+=1

print(ans)

