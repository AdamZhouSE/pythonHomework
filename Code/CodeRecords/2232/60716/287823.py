import itertools
def reach(index:int):
    if not index in getans:
#        print("add:{}".format(index))
        getans.append(index)
        for j in range(len(paths)):
            if paths[j][0]==index:
                reach(paths[j][1])
    else:
#        print("already added:{}".format(index))
        return
num = int(input())
#martix = [[0 for i in range(num)] for j in range(num)]
paths = list()
for i in range(num):
    strs = input().split()
    temp = [int(j) for j in strs]
    for t in temp:
        if t>0:
            paths.append([i,t-1])
reachpoint = list()
for i in range(num):
    getans = list()
    reach(i)
    reachpoint.append(getans)
stop = False
index = 0
need = 0
for i in range(1,num+1):
    if len(reachpoint[i-1])<num:
        need+=1
    for lists in itertools.combinations(reachpoint,i):
        temp = list()
        for j in lists:
            temp.extend(j)
        setli = list(set(temp))
        if len(setli)==num:
            index = i
            stop = True
            break
    if stop: break
print(index)
if need==0:
    print(need+1)
else:
    print(need)