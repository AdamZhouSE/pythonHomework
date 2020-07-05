def arrange(op,l,r):
    global a
    b = a[l:r+1]
    b1 = a[:l]
    b2 = a[r+1:]
    if op==0:
        b.sort()
    else:
        b.sort(reverse=True)
    a = []
    for i in b1:
        a.append(i)
    for i in b:
        a.append(i)
    for i in b2:
        a.append(i)
    return

n,m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
for k in range(m):
    op,l,r = [int(i) for i in input().split()]
    arrange(op,l-1,r-1)
q = int(input())-1
print(a[q])