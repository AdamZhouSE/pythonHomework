def filter():
    restaurant_info=list(eval(input()))
    isVeganfriendly=int(input())
    maxPrice=int(input())
    maxDistance=int(input())
    tempfilterRes=[]
    res=[]
    if isVeganfriendly==1:
        for restaurant in restaurant_info:
            if restaurant[2]==1 and restaurant[3]<=maxPrice and restaurant[4]<=maxDistance:
                tempfilterRes.append(restaurant)
    tempfilterRes=sorted(tempfilterRes, key=(lambda tempfilterRes:[tempfilterRes[1], tempfilterRes[0]] ), reverse=True)
    for restaurant in tempfilterRes:
        res.append(restaurant[0])
    print(res)

if __name__=='__main__':
    filter()