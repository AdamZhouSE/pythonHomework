#30
from itertools import combinations

T = int(input())
for i in range(0,T):
    n = int(input())
    ori = input().replace(",","")
    #print(ori)
    ori = ori.split(" ")
    #print(ori)
    num = [int(item) for item in ori if item != '']
    l = list(combinations(num,2))
    outcome = []
    for j in range(0,len(l)):
        tar = l[j]
        for k in range(j+1,len(l)):
            if sum(tar) == sum(l[k]):
                outcome.append(tar)
                outcome.append(l[k])
                break
    if len(outcome) == 0:
        print("no pairs")
        exit(0)
    a = num.index(outcome[0][0])
    b = num.index(outcome[0][1])
    c = num.index(outcome[1][0])
    d = num.index(outcome[1][1])
    print(str(a)+" "+str(b)+" "+str(c)+" "+str(d))