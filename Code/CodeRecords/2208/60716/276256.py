#没有理解题意
ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(j) for j in strs]
    aplist = list()
    anslist = list()
    for j in range(len(lists)):
        aplist.append(lists[j])
        if len(aplist)==1 or min(aplist)==lists[j]:
            anslist.append(-1)
            continue
        else:
            templist = list()
            for t in range(len(aplist)-1):
                templist.append(aplist[t]+len(aplist)-t)
            tempmin = min(templist)
            templist.reverse()
            k = len(aplist)-2-templist.index(tempmin)
            anslist.append(aplist[k])
    ans.append(anslist)
for i in ans:
    for k in range(len(i)):
        print(i[k],end=' ') if k!=len(i)-1 else print(i[k])