def canShip(weights: list, D: int, limit: int) -> bool:
    cur = limit
    for weight in weights:
        if weight > limit:
            return False
        if cur < weight:
            cur = limit
            D -= 1
        cur -= weight
    return D > 0

weights=list(map(int,input()[1:-1].split(",")))
D=int(input())
totalWeight=sum(weights)
limit=0
while limit<totalWeight:
    mid=(limit+totalWeight)//2
    if canShip(weights,D,mid):
        totalWeight=mid
    else:
        limit=mid+1
print(limit)