def docClinic(l):
    n = l[0]
    x = l[1]
    la = x*(n-1)
    lv = 10*(n-1)
    wait = lv-la
    print(wait)
    

t = int(input())
for i in range(0, t):
    l = list(map(int, list(input().split())))
    docClinic(l)