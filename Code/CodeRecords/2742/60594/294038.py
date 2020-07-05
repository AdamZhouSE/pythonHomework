n=int(input())
zc=[[]]
for i in range(n):
    row=[int(n) for n in input().split()]
    banben=row[0]
    fangfa=row[1]
    x=row[2]
    if fangfa==1:
        zs=zc[banben].copy()
        zs.append(x)
    elif fangfa==2:
        zs=zc[banben].copy()
        zs.remove(x)
    elif fangfa==3:
        zs=zc[banben].copy()
        zs.sort()
        print(zs.index(x)+1)
    elif fangfa==4:
        zs=zc[banben].copy()
        zs.sort()
        print(zs[x-1])
    elif fangfa==5:
        zs=zc[banben].copy()
        zs.sort()
        muqian=-2147483647
        for j in zs:
            if j<x:
                muqian=j
        print(muqian)
    elif fangfa==6:
        zs = zc[banben].copy()
        zs.sort()
        muqian = 2147483647
        for j in zs:
            if j > x:
                muqian = j
                break
        print(muqian)
    zc.append(zs)