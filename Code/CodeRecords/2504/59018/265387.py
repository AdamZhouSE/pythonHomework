from collections import defaultdict

dict=defaultdict(list)
info1=eval(input())
print(type(info1[0]))
info=[list(x) for x in info1]
K=int(input())
for i in range(len(info)):
    far=info[i][0]*info[i][0]+info[i][1]*info[i][1]
    if far not in dict:
        dict[far].append(i)
        