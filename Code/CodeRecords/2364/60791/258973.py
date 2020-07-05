def A(m,n):
    if n == 0:
        return 1
    else:
        return A(m,n-1)*(m-n+1)
    

N = int(input())
L = list(map(int,str(N+1)))
res = 0
n = len(L)

for i in range(1,n):
    res += 9*A(9,i-1)

seen = set()
for i, x in enumerate(L):
    temp = sum( y not in seen for y in range(0 if i else 1,x))
    res += temp*A(9-i,n-i-1)
    if x in seen:
        break
    seen.add(x)
print(N-res)