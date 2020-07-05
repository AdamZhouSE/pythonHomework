def canBuy(evidences,messages,n):
    money=0
    people=[]
    path=[]
    for i in range(len(messages)):
        money+=messages[i][1]
        for j in range(len(evidences)):
            if evidences[j][0]==messages[i][0]:
                    path.append(evidences[j])
    ind=0
    while ind<len(path):
        if path[ind][0] not in people:
            people.append(path[ind][0])
        if path[ind][1] not in people:
            people.append(path[ind][1])
        for i in range(len(evidences)):
            if evidences[i][0]==path[ind][1] and evidences[i] not in path:
                path.append(evidences[i])
        ind+=1
    canot=[]
    for i in range(n):
        if i+1 not in people:
            canot.append(i+1)
    if len(canot)!=0:
        return ["NO",min(canot)]
    else:
        res=["YES",money]
        for i in range(len(messages)):
            tem=canBuy(evidences,messages[0:i]+messages[i+1:len(messages)],n)
            if tem[0]=="YES" and tem[1]<res[1]:
                res[1]=tem[1]
        return res
n=int(input())
p=int(input())
messages=[]
evidences=[]
for i in range(p):
    messages.append(list(map(int,input().split())))
r=int(input())
for i in range(r):
    evidences.append(list(map(int,input().split())))
res=canBuy(evidences,messages,n)
print(res[0])
print(res[1])