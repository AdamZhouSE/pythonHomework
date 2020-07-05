list=list(input())
n=len(list)
for i in range(n):
    for j in range(0,n-i-1):
        if list[j][0]>list[j+1][0]:
            list[j],list[j+1]=list[j+1],list[j]
res=[]
for i in range(0,n-1):
    if list[i][1]<list[i+1][0]:
        res.append(list[i])
    else:
        if list[i][1]<=list[i+1][1]:
            list[i+1]=[list[i][0],list[i+1][1]]
        else:
            list[i + 1] = [list[i][0], list[i][1]]
res.append(list[n-1])
print(res)