def matchVegan(selector,restaurant):
    if (selector==1)and(restaurant==0):
        return False
    return True
restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
for restaurant in restaurants:
    if (not matchVegan(veganFriendly,restaurant[2]))or(restaurant[3]>maxPrice)or(restaurant[4]>maxDistance):
        restaurants.remove(restaurant)
restaurants=sorted(restaurants,key=lambda x:(x[1],x[0]),reverse=True)
selected=[]
for restaurant in restaurants:
    selected.append(restaurant[0])
print(selected)