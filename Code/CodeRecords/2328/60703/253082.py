import itertools
numList = [int(x) for x in input().split(",")]
pairs = list(itertools.permutations(numList))
pairs = list(set(pairs))
Pairs  =[]
for iii in pairs:
    h = iii[0]*10+iii[1]
    m = iii[2]*10+iii[2]
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
    
    print(MAX[0],end="")
    print(":", end="")
    print(MAX[1])