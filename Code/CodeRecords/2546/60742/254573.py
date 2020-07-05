t = int(input())
def getN(n):
    if n==0 or n==1 or n==2:
        return 1
    return getN(n-2)+getN(n-3)
for k in range(t):
    n = int(input())
    print(getN(n))