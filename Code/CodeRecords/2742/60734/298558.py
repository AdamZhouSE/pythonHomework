n = int(input())
versions = [[]]
for i in range(n):
    v, opt, x = input().split(' ')
    v, opt, x= int(v), int(opt), int(x)
    ver = versions[v].copy()
    if opt == 1:
        ver.append(x)
    elif opt == 2:
        ver.remove(x)
    elif opt == 3:
        print(ver.index(x)+1)
    elif opt == 4:
        print(ver[x-1])
    elif opt == 5:
        pre = -2**31+1
        for num in ver:
            if num < x:
                pre = num
        print(pre)
    elif opt == 6:
        succ = 2**31
        for num in ver[::-1]:
            if num>x:
                succ = num
        print(succ)
    versions.append(sorted(ver))