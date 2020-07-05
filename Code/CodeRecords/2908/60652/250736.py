N = int(input())
l = []
for i in range(0, N):
    s = input().replace(' ','')
    d = {}
    for i in s:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1
    l.append(d)
num = 0
L = []
for dic in l:
    if dic not in L:
        L.append(dic)
        num += 1
print(num,end="")