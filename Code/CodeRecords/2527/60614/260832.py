restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
for i in restaurants:
    if veganFriendly==1:
        if i[2]!=1:
            i[0]=0
            continue
    if i[3]>maxPrice or i[4]>maxDistance:
        i[0]=0
        continue
restaurants.sort(key=lambda x:(-x[1],-x[0]))
result=[]
for i in range(len(restaurants)):
    if restaurants[i][0]!=0:
        result.append(restaurants[i][0])
print(result)