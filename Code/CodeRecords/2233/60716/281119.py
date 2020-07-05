import itertools
def reach(index:int):
    if not index in fans:
        fans.append(index)
        for j in range(len(num)):
            if lists[index][j]==1:
                reach(j)
    else:
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
        if len(reachcap)==n:
            break
    index+=1
print(index)