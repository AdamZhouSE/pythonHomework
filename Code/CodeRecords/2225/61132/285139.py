def f1(l):
    return [-x for x in l]

def f2(l):
    return [-x if x%2==0 else x for x in l]

def f3(l):
    return [x if x%2==0 else -x for x in l]

def f4(l):
    return [-x if x%3==1 else x for x in l]

def itera(f,x,n):
    for i in range(n):
        x=f(x)
    return x


n=int(input())
m=int(input())
l=list(range(1,n+1))
rl=[]
for i in range(0,m+1):
    tmp=l[:]
    tmp= itera(f1,tmp,i)
    for j in range(0,m+1-i):
        tmp1=tmp[:]
        tmp1 = itera(f2, tmp1, j)
        for k in range(0,m+1-i-j):
            tmp2=tmp1[:]
            tmp2 = itera(f3, tmp2, k)
            tmp2 = itera(f4, tmp2, m-i-j-k)
            if tmp2 not in rl:
                rl.append(tmp2)
print(len(rl))