n=int(input())
rcb=[]
for i in range(n):
    row=input().split()
    if row[0]=='A':
        start=int(row[1])
        end=int(row[2])
        zc=[]
        for j in rcb:
            if (j[0]>=start and j[0]<=end) or (j[1]>=start and j[1]<=end):
                continue
            else:
                zc.append(j)
        print(len(rcb)-len(zc))
        rcb=zc.copy()
        rcb.append([start,end])
    elif row[0]=='B':
        print(len(rcb))