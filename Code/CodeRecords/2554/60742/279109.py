n = int(input())
a = [0]*10000
time = []
res = 0
for t in range(n):
    s = [int(i) for i in input().split()]
    time.append(s)
    for i in range(s[0],s[1]):
        a[i] += 1
for i in time:
    tmp = 0
    for j in range(i[0],i[1]):
        a[j] -= 1
    for j in a:
        if j!=0:
            tmp += 1
    if tmp>res:
        res = tmp
    for j in range(i[0],i[1]):
        a[j] += 1
print(res,end='')