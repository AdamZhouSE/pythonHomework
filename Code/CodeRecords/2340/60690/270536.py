n=int(input())
res=[]
for i in range(n):
    num=int(input())
    list=input().split(" ")
    for j in range(num): list[j]=int(list[j])

    wall=0
    if list[0]>= list[-1]: wall=list[-1]
    else: wall=list[0]
    total=0
    higher=[]
    for j in range(1,num):
        if list[j]<=wall:
            total+=wall-list[j]
        else:
            higher.append(j)
    if len(higher)>1:
        for j in range(len(higher)-1):
            wall_=0
            if list[higher[j]]>=list[higher[j+1]]:wall_=list[higher[j+1]]
            else:wall_=list[higher[j]]
            total+=(wall_-wall)*(higher[j+1]-higher[j]-1)
    res.append(total)
for e in res:print(e)