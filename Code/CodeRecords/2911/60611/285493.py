import sys
l=[]
l.append(list(map(int,input().split(" "))))
for i in range(l[0][1]+1):
    l.append(list(map(int,input().split(" "))))
tag=[]
if l[0][1]==0:
    print(sum(l[1]))
elif sum(l[1])==0:
    print(0)
else:
    money=0
    tag.append(l[2])
    for i in range(3,l[0][1]+2):
        if l[i][0] in tag[-1]:
            tag[-1].append(l[i][1])
        else:
            tag.append(l[i])
    for i in tag:
        count=sys.maxsize
        for j in i:
            if l[1][j-1]<count:
                count=l[1][j-1]
        money+=count
    flag=[0 for i in range(l[0][0])]
    for i in tag:
        for j in i:
            flag[j-1]=1
    for i in range(len(flag)):
        if flag[i]==0:
            money+=l[1][i]
    print(money)