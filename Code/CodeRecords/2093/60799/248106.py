import math
n, k = int(input()), int(input())-1
nList = [i for i in range(1, n + 1)]
n -= 1
MUL = math.factorial(n)
res = []
ptr = int(k/MUL)
while n != 0:
    res.append(nList[ptr])
    nList.pop(ptr)
    k = k % MUL
    MUL = int(MUL/n)
    n -= 1
    ptr = int(k / MUL)
print(''.join(str(i) for i in res+nList))