n=int(input())
for i in range(0,n):
    sz=int(input())
    list1=list(map(int,input().split(' ')))
    temp=[]
    list2=[]
    for t in list1:
        temp.append(t)
        if len(temp)==sz:
            list2.append(temp)
            temp = []
    list3=[]
    for m in range(0,sz):
        for n in range(sz-1,-1,-1):
            list3.append(list2[n][m])
    for t in range(0,sz*sz):
        if t!=sz*sz-1:
            print(list3[t],end=' ')
        else:
            print(list3[t],end=' ')
            print()