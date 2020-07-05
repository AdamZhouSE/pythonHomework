def Test():
    restaurants=eval(input())
    vagetable=int(input())
    maxPrice=int(input())
    maxDistance=int(input())
    i=0
    while(i<len(restaurants)):
        temp=restaurants[i]
        if(temp[2]==0 and vagetable==1) or temp[3]>maxPrice or temp[4]>maxDistance:
            restaurants.remove(temp)
        else:
            i=i+1
    restaurants=sorted(restaurants,key=lambda x:x[1],reverse=True)
    result=[]
    for x in restaurants:
        result.append(x[0])
    print(result)
if __name__ == "__main__":
    Test()