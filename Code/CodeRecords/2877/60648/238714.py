import math
n=input()
n=int(n)
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
result=0
for x in ls:
    result=result+math.fabs(x)
print(result)
    