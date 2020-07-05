restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
temp=[]
if veganFriendly==1:
    for restaurant in restaurants:
        if restaurant[2]==1:
            temp.append(restaurant)
else:
    temp=restaurants
temp=[i for i in temp if i[3]<=maxPrice and i[4]<=maxDistance]
temp.sort(key=lambda x: (-x[1],-x[0]))
result=[i[0] for i in temp]
print(result)