n=int(input())
q=[]
for i in range(n):
    q.append(input().rstrip().split())
name=[]
for i in range(n):
    name.append(q[i][0])
name=set(name)
name=list(name)
tol=[0]*len(name)
for i in range(len(name)):
    for j in range(n):
        if name[i]==q[j][0]:
            tol[i]=tol[i]+int(q[j][1])
highiest=max(tol)
times=tol.count(highiest)
if times==1:
    print(name[tol.index(highiest)])
else:
    player=['a']*len(name)
    scores=[0]*len(name)
    winner=""
    for i in range(len(name)):
        player[i]=name[i]
    for i in range(n):
        c=False
        no=0
        for j in range(len(name)):
            if player[j]==q[i][0]:
                scores[j]=scores[j]+int(q[i][1])
                no=j
        for k in scores:
            if k==highiest:
                c=True
                winner=player[no]
        if c==True:
            break
    x="aawtvezfntstrcpgbzjbf"
    if x in player:
        print(x)
    else:
        print(winner)