n=int(input())
name=[]
score=[]
id=[]
for i in range(n):
    id.append(i+1)
for i in range(n):
    list=input().split(' ')
    name.append(list[0])
    score.append(int(list[1]))
for i in range(n):
    for j in range(i+1,n):
        if name[i]==name[j]:
            score[i]=score[i]+score[j]
            score[j]=0
            id[i]=id[i]+id[j]
            id[j]=0
max=0
for i in range(n-1):
    for j in range(i+1,n):
        if score[i]>score[j]:
            max=i
        elif score[i]==score[j]:
            if id[i]>=id[j]:
                max=i
            else:
                max=j
        else:
            max=j
        
print(name[max])