import itertools
def reach(index:int):
    if not index in fans:
        print("add:{}".format(index))
        fans.append(index)
        for j in range(num):
            if lists[index][j]==1:
                reach(j)
    else:
        print("already added:{}".format(index))
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
while True:
    for i in itertools.combinations(sets,index):
        temp = list()
        for j in i:
            temp.extend(j)
        reachcap = list(set(temp))
        if len(reachcap)==num:
            break
    index+=1
print(index)