t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ptr = 0
    for i in range(n):
        if a[i]%2==0:
            a.insert(ptr,a.pop(i))
            ptr += 1
    for i in range(n):
        a[i] = str(a[i])
    print(' '.join(a),'')