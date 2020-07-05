n=int(input())
name=[]
points=[]
for i in range(n):
    line=input().split()
    name.append(line[0])
    points.append(int(line[1]))

answer=[points[0],0]
count=0
name2=""
for i in range(1,n):
    if name[i]!=name[i-1]:
        if name2=="":
            name2=name[i]
        count=(count+1)%2
    answer[count]+=points[i]

if answer[0]>answer[1]:
    print(name[0])
elif answer[0]<answer[1]:
    print(name2)
else:
    limit=answer[0]
    answer=[points[0],0]
    count=0
    for i in range(1,n):
        if answer[count]>=limit:
            print(name[i-1])
            break
        if name[i]!=name[i-1]:
            count=(count+1)%2
        answer[count]+=points[i]
