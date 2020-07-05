import itertools
ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split(',')
    lists = [int(j) for j in strs]
    templist = list()
    for elems in itertools.combinations(lists,4):
        for arras in itertools.permutations(elems):
            if arras[0]+arras[1] == arras[2]+arras[3]:
                temp = list()
                temp.append(lists.index(arras[0]))
                temp.append(lists.index(arras[1]))
                temp.append(lists.index(arras[2]))
                temp.append(lists.index(arras[3]))
                templist.append(tuple(temp))
    templist.sort()
    ans.append(templist[0])
for i in ans:
    for k in range(len(i)):
        print(i[k],end=' ') if k!=len(i)-1 else print(i[k])