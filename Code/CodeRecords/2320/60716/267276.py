strs = input()
k = int(input())
if k==1:
    lists = list()
    lists.append(strs)
    for i in range(len(strs)):
        strlist = list(strs)
        k = strlist.pop(0)
        strlist.append(k)
        strs = str(strlist)
        lists.append(strs)
    lists.sort()
    print(lists[0])
else:
    strlist = list(strs)
    strlist.sort()
    strs = str(strlist)
    print(strlist)