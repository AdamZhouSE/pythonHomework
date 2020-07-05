times=int(input())
for i in range(times):
    n=int(input())
    strList=list(input())
    allRecur=True
    for i in range(strList.__len__()):
        tem=strList.pop(i)
        if tem not in strList:
            print(tem)
            allRecur=False
            break
        else:
            strList.insert(i,tem)
    if allRecur:
        print(-1)