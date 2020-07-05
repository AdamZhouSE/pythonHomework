nlist = int(input())
l = []
for i in range(nlist):
    l.append(list(map(int, input().split(','))))
nflight = int(input())

lresult = []
for i in range(nflight):
    lresult.append(0)

for i in range(nlist):
    for m in range(int(l[i][0])-1, int(l[i][1])):
        lresult[m] += int(l[i][2])

print(lresult)