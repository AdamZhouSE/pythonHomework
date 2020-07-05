import itertools
def reach(index:int):
    if not index in fans:
#        print("add:{}".format(index))
        fans.append(index)
        for j in range(num):
            if lists[index][j]==1:
                reach(j)
    else:
#        print("already added:{}".format(index))
        return
num = int(input())
lists = list()
for i in range(num):
    strs = input().split()
    temp = [int(j) for j in strs]
    lists.append(temp)
sets = list()
for i in range(num):
    fans = list()
    reach(i)
    sets.append(fans)
index = 1
#print(sets)
stop = False
while True:
    for i in itertools.combinations(sets,index):
        add = 0
        for j in i:
            add+=len(j)
        if add<num:continue
#        print(i)
        temp = list()
        for j in i:
            temp.extend(j)
        reachcap = list(set(temp))
#        print(reachcap)
        if len(reachcap)==num:
            stop = True
            break
    if stop or index>=num//2:break
    index+=1
if not stop:
    index = num
    stop = False
    while True:
        for i in itertools.combinations(sets,index):
            add = 0
            for j in i:
                add+=len(j)
            if add<num:continue
#        print(i)
            temp = list()
            for j in i:
                temp.extend(j)
            reachcap = list(set(temp))
#            print(reachcap)
            if len(reachcap)==num:
                stop = True
                break
        if stop or index>=num//2:break
        index-=1
print(index)