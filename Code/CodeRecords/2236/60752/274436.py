lst=[]
sorted=False
opts=[]
for n in range(int(input())):
    i=input().split()
    opts.append(i)
    opt=int(i[0])
    val=int(i[1])

    if opt==1:
        lst.append(int(val))
        sorted=False
    if opt==2:lst.remove(int(val))
    if opt==3:
        lst.sort()
        sorted=True
        for l in range(len(lst)):
            if lst[l]==val:
                print(l+1)
                break
    if opt==4:
        if  not sorted:lst.sort()
        print(lst[val-1])
    if opt==5:
        lst.append(val)
        lst.sort()
        for ll in range(len(lst)):
            if lst[ll]==val:
                
                print(lst[ll-1])
                lst.remove(lst[ll])
                break
    if opt==6:
        lst.append(val)
        lst.sort()
        for ll in range(len(lst)):
            if lst[ll] == val:
                
                print(lst[ll + 1])
                lst.remove(lst[ll])
                break



