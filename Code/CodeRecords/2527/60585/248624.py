restraurants=eval(input())
isVeganFriendly=eval(input())
maxPrice=eval(input())
maxDistance=eval(input())
afterFilter=[]
res=[]
for i in range(len(restraurants)):
    if (restraurants[i][2]>=isVeganFriendly)&(restraurants[i][3]<=maxPrice)&(restraurants[i][4]<=maxDistance):
        afterFilter.append(restraurants[i])
afterFilter=sorted(afterFilter,key=lambda x:x[1],reverse=True)
i=0
while (i<len(afterFilter)-1):
    if afterFilter[i][1]>afterFilter[i+1][1]:
        res.append(afterFilter[i][0])
        i+=1
    else:
        j=i+1
        temp=[afterFilter[i][0]]
        while (afterFilter[j][1]==afterFilter[i][1])&(j<len(afterFilter)):
            temp.append(afterFilter[j][0])
            j+=1
        temp=sorted(temp,reverse=True)
        res.extend(temp)
        i=j
if len(afterFilter)!=len(res):
    res.append(afterFilter[-1][0])
print(res)