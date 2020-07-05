def getmax234(n):
    if n//2 + n//3 + n//4 > n:
        return getmax234(n//2) + getmax234(n//3) + getmax234(n//4)
    else:
        return n


t = int(input())
for x in range(t):
    n = int(input())
    print(getmax234(n))
