alist=list(map(int,input().split(',')))
strtmp=""
no=False
for i in range(2,-1,-1):
    if i in alist:
        strtmp+=str(i)
        alist.remove(i)
        break
else:
    no=True
if no:
    print("")
else:
    if strtmp=="2":
        for i in range(3, -1, -1):
            if i in alist:
                strtmp += str(i)
                alist.remove(i)
                break
        else:
            no=True
    else:
        for i in range(9, -1, -1):
            if i in alist:
                strtmp += str(i)
                alist.remove(i)
                break
        else:
            no=True
    if no:
        print("")
    else:
        for i in range(5,-1,-1):
            if i in alist:
                strtmp +=(":"+str(i))
                alist.remove(i)
                break
        else:
            no=True
        if no:
            print("")
        else:
            print(strtmp+str(alist[0]))