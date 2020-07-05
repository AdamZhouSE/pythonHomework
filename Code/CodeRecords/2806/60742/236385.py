def min_pay(a,p,i):
    if i==0:
        return 0
    min_price = min(p[:i])
    index = p.index(min_price)
    need_after = 0
    for j in range(index,i):
        need_after += a[j]
    return min_pay(a,p,index) + need_after*min_price

n = int(input())
a = [None]*n
p = [None]*n
for i in range(n):
    l0 = input().split()
    a[i] = int(l0[0])
    p[i] = int(l0[1])
res = min_pay(a,p,n)
print (res)