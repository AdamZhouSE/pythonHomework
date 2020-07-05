def filter(restlst,veganFriendly,maxPrice,maxDistance):
    for rest in  restlst:
        if veganFriendly==1 and rest[2]==0:
            restlst.remove(rest)
            continue
        if rest[3]>maxPrice or rest[4]>maxDistance:
            restlst.remove(rest)
            continue
    restlst = sorted(restlst,key=lambda e:e[1],reverse=True)
    return restlst

if __name__ == "__main__":
    restlst = eval(input())
    veganFriendly = int(input())
    maxPrice = int(input())
    maxDistance = int(input())
    good_rest = filter(restlst,veganFriendly,maxPrice,maxDistance)
    id = []
    for rest in good_rest:
        id.append(rest[0])
    print(id)
