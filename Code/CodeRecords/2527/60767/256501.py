def filter(veganFriendly,maxPrice,maxDistance,restaurants):
    res = []
    if(veganFriendly==1):
        for i in range(0,len(restaurants)):
            if(int(restaurants[i][2])==1 and int(restaurants[i][3])<=maxPrice and int(restaurants[i][4])<=maxDistance):
                res.append([int(restaurants[i][0]),int(restaurants[i][1])])
    else:
        for i in range(0,len(restaurants)):
            if ( int(restaurants[i][3]) <= maxPrice and int(restaurants[i][4]) <= maxDistance):
                res.append([int(restaurants[i][0]), int(restaurants[i][1])])
    res = sorted(res,key = lambda x:(x[1],x[0]),reverse=True)
    result = []
    for i in res:
        result.append(i[0])
    return result

restaurants = eval(input())
veganFridenly = int(input())
maxPrice = int(input())
maxDistance = int(input())
print(filter(veganFridenly,maxPrice,maxDistance,restaurants))
