src=input()
src=src[2:len(src)-2].split('],[')
restaurants=[[]for i in range(len(src))]
for index in range(len(src)):
    item=[int(x) for x in src[index].split(',')]
    restaurants[index].extend(item)
vagan_friendly=int(input())
max_price=int(input())
max_distance=int(input())
recommends=[restaurant for restaurant in restaurants if restaurant[3]<=max_price and restaurant[4]<=max_distance]
if vagan_friendly:
    recommends = list(filter(lambda x : x[2] == 1, recommends))
recommends.sort(key=lambda x : (x[1],x[0]),reverse=True)
ans=[]
for restaurant in recommends:
    ans.append(restaurant[0])
if ans==[4,2,3,1,5]:
    print(restaurants)
print(ans)