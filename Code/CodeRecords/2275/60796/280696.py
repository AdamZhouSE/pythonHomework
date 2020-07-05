N=int(input())
ls=[]
for i in range(N):
    ls.append(input().split(","))

row=[]
for i in range(0,N):
    s=",".join(ls[i])
    if not row.__contains__(s):
        row.append(s)

colum=[]
for i in range(0,N):
    s=""
    for j in range(N):
        s=s+ls[j][i]
        if j<N-1:
            s=s+","
    if not colum.__contains__(s):
        colum.append(s)

can=False
if len(row)==len(colum)==2:
    if N%2==0:
        if (row[0].count('1')==row[1].count('1')==N/2) and (colum[0].count('1')==colum[1].count('1')==N/2):
            can=True
    else:
        if ((row[0].count('1')==int(N/2) and row[1].count('1')==int(N/2)+1 ) or(row[0].count('0')==int(N/2) and row[1].count('0')==int(N/2)+1 )):
            if((colum[0].count('1')==int(N/2) and colum[1].count('1')==int(N/2)+1) or (colum[0].count('0')==int(N/2) and colum[1].count('0')==int(N/2)+1)):
                can=True
if can:
    result=0
    swapRow = 0  # 行交换
    time0 = []
    time1 = []
    row0 = row[0]
    row1 = row[1]
    for i in range(N):
        s = ",".join(ls[i])
        if s == row0:
            time0.append(i)
        if s == row1:
            time1.append(i)
    if N%2==1:
        if len(time0) > len(time1):
            for i in range(len(time1)):
                if time1[i] % 2 != 1:
                    swapRow = swapRow + 1
        else:
            for i in range(len(time0)):
                if time0[i] % 2 != 1:
                    swapRow = swapRow + 1
    else:
        x1=0
        x2=0
        for i in range(len(time0)):
            if time0[i]%2==0:
                x1=x1+1
            else:
                x2=x2+1
        if x1<x2:
            swapRow=x1
        else:
            swapRow=x2
    # 列交换
    swapColum = 0
    time0 = []
    time1 = []
    colum0 = colum[0]
    colum1 = colum[1]
    for i in range(N):
        s = ""
        for j in range(N):
            s = s + ls[j][i]
            if j < N - 1:
                s = s + ","
        if s == colum0:
            time0.append(i)
        if s == colum1:
            time1.append(i)
    if N % 2 == 1:
        if len(time0) > len(time1):
            for i in range(len(time1)):
                if time1[i] % 2 != 1:
                    swapColum= swapColum + 1
        else:
            for i in range(len(time0)):
                if time0[i] % 2 != 1:
                    swapColum = swapColum + 1
    else:
        x1 = 0
        x2 = 0
        for i in range(len(time0)):
            if time0[i] % 2 == 0:
                x1 = x1 + 1
            else:
                x2 = x2 + 1
        if x1 < x2:
            swapColum = x1
        else:
            swapColum = x2
    result=swapColum+swapRow
    print(result)

else:
    print(-1)












