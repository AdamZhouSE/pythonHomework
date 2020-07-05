from collections import defaultdict

dict=defaultdict(list)
info1=eval(input())
K=int(input())
for i in range(len(info)):
    far=info[i][0]*info[i][0]+info[i][1]*info[i][1]
    dict[far].append(i)
        