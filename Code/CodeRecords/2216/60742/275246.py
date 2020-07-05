def GCD(n,m):#默认n,m>0
    if m>n:
        tmp=m
        m=n
        n=tmp
    if m==0:
        return n
    r = n%m
    return GCD(m,r)
def LCM(n,m):
    if m>n:
        tmp=m
        m=n
        n=tmp
    res = n
    while not (res%n==0 and res%m==0):
        res += 1
    return res

l = input().replace('-','+-').split('+')
if l[0]=='':
    l.pop(0)
n = len(l)
fenzi = []
fenmu = []
for i in l:
    s = [int(j) for j in i.split('/')]
    fenzi.append(s[0])
    fenmu.append(s[1])
lcm = fenmu[0]
for i in fenmu:
    lcm = LCM(lcm,i)
for i in range(n):
    fenzi[i] *= lcm//fenmu[i]
fenzi_res = 0
for i in fenzi:
    fenzi_res += i
if fenzi_res==0:
    print('0/1')
elif fenzi_res<0:
    gcd = GCD(lcm,-fenzi_res)
    lcm = lcm//gcd
    fenzi_res = fenzi_res//gcd
    print(fenzi_res,end='')
    print('/',end='')
    print(lcm)
else:
    gcd = GCD(lcm,fenzi_res)
    lcm = lcm//gcd
    fenzi_res = fenzi_res//gcd
    print(fenzi_res,end='')
    print('/',end='')
    print(lcm)