n, c, m = input().split()
n, c, m = int(n), int(c), int(m)

flowers = list(map(int, input().split()))

for i in range(m):
    l, r = input().split()
    l, r = int(l), int(r)
    get = flowers[l-1:r]
    ans = 0
    for i in range(c):
        if get.count(i) > 1:
            ans+=1
    print(ans)