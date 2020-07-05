def rank(oc):
    for index1 in range(len(oc)):
        for index2 in range(index1 + 1, len(oc)):
            if oc[index1][0] > oc[index2][0]:
                tmp = oc[index1]
                oc[index1] = oc[index2]
                oc[index2] = tmp
def rank1(oc):
    for index1 in range(len(oc)):
        for index2 in range(index1 + 1, len(oc)):
            if oc[index1][1] > oc[index2][1]:
                tmp = oc[index1]
                oc[index1] = oc[index2]
                oc[index2] = tmp

num=[int(n) for n in input().split()]
n=num[0]
c=num[1]
f=num[2]
oc=[]
for i in range(c):
    row=[int(n) for n in input().split()]
    oc.append(row)
rank(oc)
max=-1
for i in range(int((n-1)/2),len(oc)-int((n-1)/2)):
    qian=0
    hou=0
    zc=[]
    for index in range(i):
        zc.append(oc[index])
    rank1(zc)
    for j in range(int((n-1)/2)):
        qian+=zc[j][1]
    zc=[]
    for index in range(1,len(oc)-i):
        zc.append(oc[i+index])
    rank1(zc)
    for j in range(int((n-1)/2)):
        hou+=zc[j][1]
    if qian+hou+oc[i][1]<=f and oc[i][0]>max:
        max=oc[i][0]
print(max,end='')