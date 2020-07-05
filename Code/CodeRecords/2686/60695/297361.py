t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    a = input().split(" ")
    a = list(map(int, a))
    if k == 1:
        r = []
        for i in range(n-1):
            for j in range(i+1,n):
                if a[j]- a[i]>0:
                    r.append(a[j]- a[i])
        r = sorted(r)
        if len(r)==0:
            print(0)
        else:
            print(r[len(r)-1])
    else:
        nega = []
        for i in range(1, n):
            if a[i] - a[i - 1] < 0:
                nega.append(a[i - 1] - a[i])
        nega = sorted(nega, reverse=True)
        res = a[n - 1] - a[0]
        i = 0
        k -= 1
        while k > 0 and i < len(nega):
            res += nega[i]
            i += 1
            k -= 1
        print(res)
