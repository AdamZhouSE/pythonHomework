k = int(input())
for i in range(k):
    n = int(input())
    l = input().split()
    for i in range(n):
        l[i] = int(l[i])
    l.sort(reverse=True)
    res = 0
    while res<n and res+1<=l[res]:
        res += 1
    print (res)