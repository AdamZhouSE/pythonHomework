def getMax(n):
    if n == 0 or n == 1:
        return n
    else:
        return max(getMax(n // 2) + getMax(n // 3) + getMax(n // 4), n)
    
n = int(input())
for i in range(n):
    k = int(input())
    print(getMax(k))