times=int(input())
for i in range(times):
    n=int(input())
    strList=list(input())
    for i in range(n):
        tem=strList.pop(i)
        if tem not in strList:
            print(tem)
            break
        else:
            strList.insert(i,tem)