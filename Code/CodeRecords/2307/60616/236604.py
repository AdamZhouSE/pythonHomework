num=int(input())
for i in range (num):
    lists = []
    ans = []
    doExist = False
    n=int(input())
    tmpLists=input().split(' ')
    tmpDic={}
    lists.append(tmpLists)
    for tmpList in tmpLists:
        tmpDic[tmpList]=tmpLists.count(tmpList)
    for key,value in tmpDic.items():
        if(value>n/2):
            doExist=True
            break
    for key,value in tmpDic.items():
        if(value>n/2):
            ans.append(key)
    if (doExist):
        print(" ".join(str(i) for i in ans))
    else:
        print('-1')