astr=input()
alist=astr.split()
pointnum=int(alist[0])
linenum=int(alist[1])
start=int(alist[2])
end=int(alist[3])
verlist=[]
for i in range(pointnum):
    verlist.append([999]*pointnum)
for i in range(linenum):
    str0=input()
    list0=str0.split()
    st=int(list0[0])
    en=int(list0[1])
    leng=int(list0[2])
    verlist[st-1][en-1]=leng
for  i in range(pointnum):
    for j in range(pointnum):
        for k in range(pointnum):
            if verlist[i][j] > verlist[i][k]+verlist[k][j]:
                verlist[i][j] = verlist[i][k]+verlist[k][j]
print(verlist[start-1][end-1])
