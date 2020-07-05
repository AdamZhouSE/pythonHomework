ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
#    print(strs)
    lists = [int(k) for k in strs]
    templist = list()
    while True:
        if len(lists)==0:break
        temp = max(lists)
        if temp == lists[0] and lists.count(lists[0])==1: templist.append(-1)
        else:
            for j in range(1,len(lists)):
                if lists[j]>=lists[0]:
                    templist.append(lists[j])
                    break
        lists.pop(0)
    ans.append(templist)
#    if templist==[-1,4,4,-1]: print(strs)
for i in ans:
    for k in range(len(i)):
        print(i[k],end=' ') if k!=len(i)-1 else print(i[k])