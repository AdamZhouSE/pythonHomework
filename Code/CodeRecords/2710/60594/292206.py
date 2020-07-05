num=[int(n) for n in input().split()]
n=num[0]
q=num[1]
xc=[]
for i in range(q):
    row=input().split()
    if row[0]=='M':
        chezhan=int(row[1])
        nianling=int(row[2])
        xc.append([chezhan,nianling])
    elif row[0]=='D':
        chezhan=int(row[1])
        nianling=int(row[2])
        min=100
        for j in xc:
            if j[0]<=chezhan and j[1]>=nianling and j[1]<min:
                min=j[1]
        print(min)