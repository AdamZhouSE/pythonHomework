restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
for restaurant in restaurants:
    if (restaurant[2]!=veganFriendly)or(restaurant[3]>maxPrice)or(restaurant[4]>maxDistance):
        restaurants.remove(restaurant)
sorted(restaurants,key=lambda x:(x[1],x[0]),reverse=True)
selected=[]
for restaurant in restaurants:
    selected.append(restaurant[0])
print(selected)