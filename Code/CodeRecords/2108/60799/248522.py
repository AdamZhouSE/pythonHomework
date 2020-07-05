n = int(input())
L = len(str(n))
b = 10**(L-1)
aList = [int(i*(10**(i-1))) for i in range(L)]
res = 0
while b != 0:
    first = int(n/b)
    res += aList.pop() * first
    res += min(b, n-b+1)
    n = n % b
    b = int(b/10)
print(res)