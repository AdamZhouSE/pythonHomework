import itertools
ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split(',')
    strs = str(strs).split()
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
    if len(templist)==0:
        print('no pairs')
    else:
        i = list(templist[0])
        for k in range(len(i)):
            print(i[k],end=' ') if k!=len(i)-1 else print(i[k])