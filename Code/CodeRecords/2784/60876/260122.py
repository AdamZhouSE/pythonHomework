n,m=map(int,input().split(" "))
winners=[]
winner=[]
for i in range(0,m):
    temp=list(map(int,input().split(" ")))
    max=0
    it=0
    for index in range(0,n):
        if temp[index]>max:
            it=index
            max=temp[index]
    winners.append(it+1)
    if (it+1) not in winner:
        winner.append(it+1)
winner.sort()
result=winner[0]
max=0
for item in winner:
    temp=0
    while item in winners:
        i=winners.index(item)
        temp+=1
        del winners[i]
    if temp>max:
        max=temp
        result=item
print(result)
