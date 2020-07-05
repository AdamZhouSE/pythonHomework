def solve(path, b):
    n = len(path)
    temp = copy(path)
    for i in range(n):
        for k in range(n):
            for m in range(n):
                if m!=i and path[i][k] != 1000 and path[k][m] != 1000 and path[i][m] == 1000:
                    temp[i][m] = b
                    temp[m][i] = b
    return temp


def find(path, res, k):
    n = len(path)
    for i in range(n):
        res.append(0)
    shortest = []
    for i in range(n - 1):
        m =min(path[k],shortest)
        temp =[]
        already=[]
        for p in shortest:
            already.append(p[1])
        already.append(k)
        n=mini(path, shortest,temp,k)

        if m<n:
            val = m
            for p in range(len(path[k])):
                if path[k][p]==m and p not in already:
                    ind = p
                    break
        else:
            val = n
            ind = temp[-1]
        shortestforever = [val, ind]
        shortest.append(shortestforever)
    for i in shortest:
        res[i[1]] = i[0]


def mini(path, shortest,res,k):
    temp = []
    for  i in shortest:
        temp.append(i[1])
    temp.append(k)
    num =len(path)
    min = 1000
    sum = 0
    for i in shortest:
        for k in range(num):
            sum = i[0]+path[i[1]][k]
            if sum < min and k not in temp:
                min = sum
                res.append(k)
    return min
def min(a,b):
    temp = []
    for i in b:
        temp.append(i[1])
    min = 1000
    for i in range(len(a)):
        if a[i] <min and i not in temp:
            min = a[i]
    return min

def copy(l):
    res = []
    for i in l:
        temp = []
        for k in range(len(i)):
            if i[k]==1000:
                temp.append(2000)
            else:
                temp.append(i[k])
        res.append(temp)
    return res


im = input().split(" ")
for i in range(len(im)):
    im[i] = int(im[i])
n = im[0]
m = im[1]
k = im[2]
a = im[3]
b = im[4]
all = []
path = []
for i in range(m):
    all.append(input().split(" "))
for i in range(n):
    temp = []
    for y in range(n):
        temp.append(1000)
    path.append(temp)
for i in all:
    path[int(i[0]) - 1][int(i[1]) - 1] = a
for u in range(n):
    for p in range(n):
        if path[u][p] == a:
            path[p][u] = a
        if path[p][u] == a:
            path[u][p] = a
path = solve(path, b)
res = []
find(path, res, k-1)
for i in res:
    print(i)
