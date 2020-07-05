ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(k) for k in strs]
    templist = list()
    while True:
        if len(lists)==0:break
        temp = max(lists)
        if temp == lists[0]: templist.append(-1)
        else:templist.append(temp)
        lists.pop(0)
    ans.append(templist)
for i in ans:
    for k in range(len(i)):
        print(i[k],end=' ') if k!=len(i)-1 else print(i[k])