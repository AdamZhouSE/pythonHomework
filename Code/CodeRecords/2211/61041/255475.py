arrin = input().split()
n = int(arrin[0])
k = int(arrin[1])
alph = []
parent = []
want = []
name = []
for i in range(0,n):
    temparr = input().split()
    alph.append(temparr[0])
    parent.append(int(temparr[1]))
for j in range(0,k):
    want.append(input())
name.append(alph[0])
for p in range(1,len(alph)):
    temp = alph[p]+name[parent[p]-1]
    name.append(temp)
for x in range(0,len(want)):
    cnt = 0
    for y in range(0,len(name)):
        if len(name[y])<len(want[x]):
            continue
        elif name[y].startswith(want[x]):
            cnt+=1
        else:
            continue
    print(cnt)
    cnt = 0  