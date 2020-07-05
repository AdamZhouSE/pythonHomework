def matchVegan(selector,r_vegan):
    if (selector==1)and(r_vegan==0):
        return False
    else:
        return True
restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
s=[]
for restaurant in restaurants:
    if (matchVegan(veganFriendly,restaurant[2]))and(restaurant[3]<=maxPrice)and(restaurant[4]<=maxDistance):
        s.append(restaurant)
s=sorted(s,key=lambda x:(x[1],x[0]),reverse=True)
selected=[]
for i in s:
    selected.append(i[0])
print(selected)