import itertools
numList = [int(x) for x in input().split(",")]
pairs = list(itertools.permutations(numList))
pairs = list(set(pairs))
Pairs  =[]
for iii in pairs:
    h = iii[0]*10+iii[1]
    m = iii[2]*10+iii[3]
    if(0<=h<24 and 0<=m<60):
        Pairs.append([h,m])
if(len(Pairs)==0):
    print("")
else:
    MAX = [0,0]
    for i in Pairs:
        if(i[0]>MAX[0]):
            MAX = i
        elif(i[0]==MAX[0] and i[1]>MAX[1]):
            MAX = i
    res = ""
    if(MAX[0]<10):
        res = res+"0"+str(MAX[0])
    else:
        res = res+str(MAX[0])
    if(MAX[1]<10):
        res = res+":0"+str(MAX[1])
    else:
        res = res+":"+str(MAX[1])


    print(res)