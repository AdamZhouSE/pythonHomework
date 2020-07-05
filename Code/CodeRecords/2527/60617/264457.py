def filter():
    restaurant_info=list(eval(input()))
    isVeganfriendly=int(input())
    maxPrice=int(input())
    maxDistance=int(input())
    tempfilterRes=restaurant_info.copy()
    res=[]
    if isVeganfriendly==1:
        for restaurant in restaurant_info:
            if restaurant[2]==1 and restaurant[3]<=maxPrice and restaurant[4]<=maxDistance:
                tempfilterRes.append(restaurant)
    tempfilterRes.sort(key=(lambda tempfilterRes:[tempfilterRes[1], tempfilterRes[0]] ))
    for restaurant in tempfilterRes:
        res.append(restaurant[0])
    print(res)

if __name__=='__main__':
    filter()
