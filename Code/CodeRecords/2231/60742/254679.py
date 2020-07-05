a = []
sphenic = True
def get_divisor(n):
    for i in range(2,n+1):
        if n%i==0:
            if i in a:
                sphenic = False
                return
            else:
                a.append(i)
                get_divisor(n//i)
                break
    return
t = int(input())
for k in range(t):
    n = int(input())
    a = []
    sphenic = True
    get_divisor(n)
    if len(a)!=3:
        sphenic = False
    if sphenic:
        print('1')
    else:
        print('0')