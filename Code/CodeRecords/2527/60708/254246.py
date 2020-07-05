restaurants=eval(input())#餐厅列表
isveganFriendly=input()
maxPrice=int(input())
maxDistance=int(input())
pick=[]
for item in restaurants:
    if(isveganFriendly=="0")or(item[2]==1):
        if(item[3]<=maxPrice):
            if(item[4]<=maxDistance):
                pick.append(item)
result=[]
ID=[]
Rate=[]
for item in pick:
    ID.append(item[0])
    Rate.append(item[1])
i=0
time=len(ID)
while(i<time):
    if(len(Rate)>=1):
        maxrate=max(Rate)
    j=len(Rate)-1
    while(j>=0):
        if Rate[j]==maxrate:
            result.append(ID[j])
            ID.pop(j)
            Rate.pop(j)
        j=j-1
    i=i+1
print(result)