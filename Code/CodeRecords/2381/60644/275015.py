def baseNeg2(N):
    """
    :type N: int
    :rtype: str
    """
    res = []
    # n = N
    while N:
        N, b = divmod(N, 2)
        N = -N
        res.append(str(b))
    return "".join(res[::-1]) or "0"

import math
a1=input().split(',')
a2=input().split(',')
for i in range(0,len(a1)):
    a1[i]=int(a1[i])
for i in range(0,len(a2)):
    a2[i]=int(a2[i])
n1=0
n2=0
for i in range(0,len(a1)):
    n1=n1+math.pow(-2,len(a1)-i-1)*a1[i]
for i in range(0,len(a2)):
    n2=n2+math.pow(-2,len(a2)-i-1)*a2[i]
n1=int(n1)
n2=int(n2)
n=n1+n2
res=list(baseNeg2(n))
for i in range(0,len(res)):
    res[i]=int(res[i])
print(res)

