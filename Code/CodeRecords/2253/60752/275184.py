l1=input().split()
size=int(l1[0])
lst=list(map(int,input().split()))
for m in range(int(l1[1])):
    l2=list(map(int,input().split()))
    opt=l2[0]

    if opt==1:
        count=0
        for i in sorted(lst[l2[1]-1:l2[2]]):
            count+=1
            if i==l2[3]:
                print(count)
                break
    if opt==2:
        print(sorted(lst[l2[1]-1:l2[2]])[l2[3]-1])
    if opt==3:
        lst[l2[1]-1]=l2[2]
    if opt==4:
        lstt=lst[l2[1]-1:l2[2]].copy()
        lstt.append(l2[3])
        lstt.sort()
        for ll in range(len(lstt)):
            if lstt[ll]==l2[3]:
                print(lstt[ll-1])
                break
    if opt==5:
        lstt = lst[l2[1]-1:l2[2]].copy()
        lstt.append(l2[3])
        lstt.sort()
        for ll in range(len(lstt)):
            if lstt[ll] == l2[3]:
                print(lstt[ll + 1])
                break

