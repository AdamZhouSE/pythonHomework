#没有理解题意
ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(j) for j in strs]
    anslist = list()
    anslist.append(-1)
    for j in range(1,len(lists)):
        temp = lists[0:j]
#        print("operate:{}".format(temp))
        if min(temp)>=lists[j]:
            anslist.append(-1)
            continue
        temp.reverse()
        for t in temp:
            if t<lists[j]:
                anslist.append(t)
                break
    ans.append(anslist)
#for i in ans:
#    print(i)
for i in ans:
    for k in range(len(i)):
        print(i[k],end=' ')
    print("")