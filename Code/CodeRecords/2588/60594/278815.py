def panduan(n):
    if n==4:
        return False
    shifou=True
    for i in range(2,int(n/2)):
        if n%i==0:
            shifou=False
            break
    return shifou
def judge(n,fianl):
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            fianl.append(i)
            return judge(n / i,fianl)
    final.append(int(n))
n=int(input())
for i in range(n):
    a=int(input())
    if panduan(a):
        print(0)
    else:
        final = []
        judge(a, final)
        zc = []
        for j in final:
            if j > 9:
                zc.append(j)
                k = j
                while k > 9:
                    final.append(k % 10)
                    k = int(k / 10)
                final.append(k)
        for j in zc:
            final.remove(j)
        oc = 0
        for j in final:
            oc += j
        oc2 = 0
        zc = []
        while a > 9:
            zc.append(a % 10)
            a = int(a / 10)
        zc.append(a)
        for j in zc:
            oc2 += j
        if oc == oc2:
            print(1)
        else:
            print(0)














