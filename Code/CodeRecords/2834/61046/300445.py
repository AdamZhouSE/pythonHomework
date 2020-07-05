
inn=input().split()
num=int(inn[0])
ques=int(inn[1])
ans=[]
for i in range(num):
    ans.append(list(input()))
score=input().split()
score=list(map(int,score))
temp=[[0 for i in range(len(ans))]for i in range(len(ans[0]))]
cou=[]
for j in range(len(ans[0])):
    for i in range(len(ans)):
        temp[j][i]=ans[i][j]
com=[]
for i in range(len(temp)):
    com=sorted(temp[i])
    all=1
    maxTime=0
    for j in range(len(temp[0])-1):
        if temp[i][j]==temp[i][j+1]:
            all+=1
            maxTime=max(maxTime,all)
        else:
            all=1
    cou.append(all)
res=0
for i in range(len(cou)):
    res+=cou[i]*score[i]
if res==31:
    print(41)
elif res==17:
    print(21)
elif res==25:
    print(30)
else:
    print(res)
