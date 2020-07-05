import copy
n,m,q=map(int,input().split(' '))
instrctions=[]
house=[[] for _ in range(m)]
have_done=[]
def go(i,j):
    global house
    for k in house:
        if(i in k):
            k.remove(i)
            break
    house[j].append(i)
    house[j].sort()
def experiment(l,r):
    global house,have_done
    result=0
    for i in range(l-1,r):
        if(house[i]!=[] and house[i] not in have_done):
            have_done.append(copy.deepcopy(house[i]))
            result+=len(house[i])
    return result
for i in range(n):
    house[0].append(i)
for i in range(q):
    instrctions.append(input().split(' '))
for i in instrctions:
    if(i[0]=='C'):
        go((int)(i[1])-1,(int)(i[2])-1)
    elif(i[0]=='W'):
        print(experiment((int)(i[1]),(int)(i[2])))

