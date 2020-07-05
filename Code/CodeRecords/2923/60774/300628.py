def getKey(elem):
    return elem[1]

s = input().split(' ')
n = int(s[0])
q = int(s[1])
numLst = list(map(int,input().split(' ')))
numLst.sort(reverse = True)
weight = [[x,0] for x in range(0,n)]
for i in range(0,q):
    s = input().split(' ')
    start = int(s[0])
    end = int(s[1])
    for j in range(start - 1,end):
        weight[j][1] = weight[j][1] + 1
weight.sort(key = getKey,reverse = True)
sumq = 0
t = 0
for w in weight:
    if(w[1] == 0):
        break
    else:
        sumq = sumq + w[1] * numLst[t]
        t = t + 1
print(sumq)