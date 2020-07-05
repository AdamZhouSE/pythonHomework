n = int(input())
v = [[]]
for i in range(n):
    vi, opti, xi = list(map(int, input().split()))
    version = v[vi]
    newversion = version.copy()
    if opti == 1:
        newversion.append(xi)
    elif opti == 2:
        if xi in newversion:
            newversion.remove(xi)
    elif opti == 3:
        print(newversion.index(xi) + 1)
    elif opti == 4:
        print(newversion[xi - 1])
    elif opti == 5:
        if xi in newversion and newversion[0] != xi:
            print(newversion[newversion.index(xi) - 1])
        else:
            newversion.append(xi)
            newversion.sort()
            if newversion[0] == xi:
                print(-2 ** 31 + 1)
            else:
                print(newversion[newversion.index(xi) - 1])
            newversion = version.copy()
    elif opti == 6:
        if xi in newversion and newversion[-1] != xi:
            print(newversion[len(newversion) - newversion[::-1].index(xi)])
        else:
            newversion.append(xi)
            newversion.sort()
            if newversion[-1] == xi:
                print(2 ** 31)
            else:
                print(newversion[len(newversion) - newversion[::-1].index(xi)])
            newversion = version.copy()
    v.append(sorted(newversion))
    #print("vi",vi,"opti",opti,"xi",xi)
#print(v)
