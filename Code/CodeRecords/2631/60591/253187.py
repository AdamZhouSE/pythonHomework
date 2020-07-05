def sortByFirst(key):
    return key[0]

def findMax(milks):
    max = 0
    maxMilks = []
    for x in range(len(milks)):
        if(milks[x] > max):
            max = milks[x]
            maxMilks = [x]
        elif(milks[x] == max):
            maxMilks.append(x)
    return max,maxMilks

N,G = list(map(int,input().split(" ")))
milks = []
for x in range(100):
    milks.append(G)
ops = {}
while(N != 0):
    N = N - 1
    temp = input().split(" ")
    days = (int(temp[0]),int(temp[1]))
    ops[days] = eval(temp[2])
keys = list(ops.keys())
keys.sort(key= sortByFirst)
#print(keys)

max = G
maxMilks = []
cnt = 0

#print("______________")
for key in keys: # 一次操作
    milks[key[1]] += ops[key]
    #print(milks)
    temp,tempMilks = findMax(milks)
    #print(max,temp,tempMilks)
    if(temp > max):
        for temp in tempMilks:
            if(temp not in maxMilks):
                cnt += 1
        #for temp in maxMilks:
        #    if(temp not in tempMilks):
        #        cnt += 1
        maxMilks = tempMilks
    elif(max == temp):
        if(milks[key[1]] == max):
            cnt += 1
print(cnt,end = "")

