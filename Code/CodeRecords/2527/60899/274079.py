a = "".join(input().split("["))
a = "".join(a.split("]"))
a = list(map(int,a.split(",")))
restaurants = [[a[x*5+y] for y in range(5)] for x in range(len(a)//5)]
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
list1 = []
for restaurant in restaurants:
    if ((veganFriendly == 1 and restaurant[2] == 1)or veganFriendly==0 ) and (restaurant[3] <= maxPrice) and (restaurant[4] <= maxDistance):
        list1.append(restaurant)
list1.sort(key=lambda x:x[0],reverse=True)
list1.sort(key=lambda x:x[1],reverse=True)
list0 = []
for restaurant in  list1:
    list0.append(restaurant[0])
print(list0)