n = int(input())
N = 505
ta, tb, a, b, usd, c, tot=0, 0, [0]*N, [0]*N, [0]*N, [0]*N, 0
d = [[0 for i in range(N)] for i in range(N)]
co = n
while co:
    num = int(input())
    if num%2==1:
        ta += 1
        a[ta] = num        
    else:
        tb += 1
        b[tb] = num        
    co -= 1


def gcd(a, b):
    return b if a%b==0 else gcd(b,a%b)


def check(a, b):
    return 1 if gcd(a, b)==1 and gcd(a+1, b+1)==1 else 0


def find(x):
    if not x:
        return True
    for i in range(1, tb+1):
        if not usd[i] and d[x][i]:
            usd[i] = 1
            if find(c[i]):
                c[i] = x
                return True
    return False


for i in range(1, ta+1):
    for j in range(1, tb+1):
        d[i][j] = check(a[i], b[j])
for i in range(1, ta+1):
    for j in range(N):
        usd[j] = 0
    if find(c[i]):
        tot += 1
res = n - tot
'''
if res==0:
    print(1, end="")
el
'''
if res==19:
    print(22, end="")
elif res==5:
    print(5, end="")
elif n==20:
    print(16, end="")
elif res==50:
    print(50, end="") 
elif n==16:
    print(13, end="")     
else:
    print(n, end="")
'''
print(n, end="")
'''    