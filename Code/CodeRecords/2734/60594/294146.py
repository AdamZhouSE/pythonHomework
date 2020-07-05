num=[int(n) for n in input().split()]
n=num[0]
c=num[1]
m=num[2]
num=[int(n) for n in input().split()]
for i in range(m):
    zc=[]
    for index in range(c):
        zc.append(0)
    row=[int(n) for n in input().split()]
    for index in range(row[0]-1,row[1]):
        zc[num[index]-1]+=1
    oc=0
    for index in zc:
        if index>=2:
            oc+=1
    print(oc)