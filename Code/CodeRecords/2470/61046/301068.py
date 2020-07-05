num=int(input())
alist=[]
blist=[]
for i in range(num):
    alist.append(input())
    blist.append(input())
for i in range(num):
    size=int(alist[i])
    test=blist[i].split()
    change=[["0" for i in range(size)]for j in range(size)]
    final = [["0" for i in range(size)] for j in range(size)]
    ans=[]
    for i in range(size):
        for j in range(size):
            change[i][j]=test[i*size+j]
    for i in range(size):
        for j in range(size):
            final[i][j]=change[j][i]
    for i in range(size):
        for j in range(size):
            ans.append(final[i][size-1-j])
    print(str(" ".join(ans))+" ")
