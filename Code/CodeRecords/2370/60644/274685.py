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
n=int(input())
res=''
print(baseNeg2(n))
