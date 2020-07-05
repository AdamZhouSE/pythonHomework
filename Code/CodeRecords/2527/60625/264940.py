from ast import literal_eval
def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
        if not restaurants:
            return []

        res = []
        for i, rating, vF, mP, mD in restaurants:
            if not veganFriendly or (vF and veganFriendly):
                if mP <= maxPrice and mD <= maxDistance:
                    res.append([i, rating])

        return [i for i, rating in sorted(res, key=lambda x: (x[1], x[0]), reverse=True)]


s=input()
restaurants=literal_eval(s)
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
print(filterRestaurants(restaurants,veganFriendly,maxPrice,maxDistance))