def solve(restaurants:list,veganFriendlyi:int,maxPrice:int,maxDistance:int):
    if not restaurants:
        return []
    res = []
    for i,rating,vF,mp,md in restaurants:
        if not veganFriendlyi or (vF and veganFriendlyi):
            if mp<=maxPrice and md<=maxDistance:
                res.append([i,rating])

    return [i for i,rating in sorted(res,key=lambda x:(x[1],x[0]),reverse=True)]

if __name__ == '__main__':
    line = input()
    V = int(input())
    maxPrice = int(input())
    maxDistance = int(input())
    line = line[2:len(line) - 2]
    line = line.split('],[')
    for i in range(len(line)):
        line[i] = line[i].replace(',', ' ')
        line[i] = list(map(int, line[i].split()))
    print(solve(line,V,maxPrice,maxDistance))