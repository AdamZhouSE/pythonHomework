n,q=[int(i) for i in input().split()]
a=n*[n*[-1]]
for ques in range(q):
    ope=[int(i) for i in input().split()]
    if ope[0]==0:
        a[ope[1]][ope[2]]=ope[3]
        a[ope[2]][ope[1]]=ope[3]
    elif ope[0]==1:
        a[ope[1]][ope[2]]=-1
        a[ope[2]][ope[1]]=-1
    else:
        print(a[ope[1]][ope[2]])
        