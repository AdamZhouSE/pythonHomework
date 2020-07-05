n = int(input())
res = []
for i in range(0,n):
    res.append(input().split(' '))
    res[i][1] = int(res[i][1])

for i in range(0,n):
    j=i-1
    while(j!=-1):
        if res[j][0] == res[i][0]:
            res[i][1]+=res[j][1]
            break
        j-=1

mmax = 0
for i in range(0,n):
    mmax = max(mmax,res[i][1])

for i in range(0,n):
    if res[i][1] ==mmax:
        print(res[i][0])
        break