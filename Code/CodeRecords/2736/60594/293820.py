num=[int(n) for n in input().split()]
n=num[0]
m=num[1]
num=[int(n) for n in input().split()]
for i in range(m):
    row=input().split()
    if row[0]=='Q':
        l=int(row[1])
        r=int(row[2])
        k=int(row[3])
        zc=[]
        for index in range(l-1,r):
            zc.append(num[index])
        zc.sort()
        print(zc[k-1])
    elif row[0]=='C':
        x=int(row[1])-1
        y=int(row[2])
        num[x]=y