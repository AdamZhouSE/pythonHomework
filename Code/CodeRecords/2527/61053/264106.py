def filter(restlst,veganFriendly,maxPrice,maxDistance):
    good_rest = []
    for rest in  restlst:
        if veganFriendly==1 and rest[2]==0:
            continue
        if rest[3]>maxPrice or rest[4]>maxDistance:
            continue
        good_rest.append(rest)
    good_rest = good_rest[::-1]
    good_rest = sorted(good_rest,key=lambda e:e[1],reverse=True)
    return good_rest

if __name__ == "__main__":
    restlst = eval(input())
    for rest in restlst:
        for i in range(0,len(rest)):
            rest[i] = int(rest[i])
    veganFriendly = int(input())
    maxPrice = int(input())
    maxDistance = int(input())
    good_rest = filter(restlst,veganFriendly,maxPrice,maxDistance)
    id = []
    for rest in good_rest:
        id.append(rest[0])
    print(id)