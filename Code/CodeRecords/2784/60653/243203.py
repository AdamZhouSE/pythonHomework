n, m = map(int, input().split(" "))
city = []
name = [0]*n
for i in range(0, m):
    city.append([int(n) for n in input().split(" ")])
for i in range(0, m):
    mmax = 0
    for j in range(0, n):
        if city[i][j] > mmax:
            mmax = city[i][j]
    for j in range(0, n):
        if city[i][j] == mmax:
            name[j] += 1
            break
nmax = 0
for i in range(0, n):
    if name[i] > nmax:
        nmax = name[i]
for i in range(0, n):
    if name[i] == nmax:
        print(i+1)
        break