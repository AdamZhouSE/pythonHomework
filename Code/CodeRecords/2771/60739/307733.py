import math
def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n

n = int(input())
for i in range(n):
    k = int(input())
    if isSqr(k):
        print(1)
    else:
        print(0)