import re
s=input().split("],[")
s[0]=s[0].strip("[")
s[len(s)-1]=s[len(s)-1].strip(']')
lis=[list()]*len(s)
for i in range(0,len(s)):
    lis[i]=s[i].split(",")
for i in range(0,len(lis)):
    for j in range(0,len(lis[0])):
        lis[i][j]=int(lis[i][j])
ve=int(input())
ma=int(input())
max=int(input())
def filterRestaurants( restaurants, veganFriendly, maxPrice, maxDistance):
    if not restaurants:
        return []
    res = []
    for i in range(0,len(restaurants)):
        if not veganFriendly or (restaurants[i][2] and veganFriendly):
            if restaurants[i][3] <= maxPrice and restaurants[i][4] <= maxDistance:
                res.append([restaurants[i][0], restaurants[i][1]])
    return [i for i, rating in sorted(res, key = lambda x:(x[1], x[0]), reverse = True)]
print(filterRestaurants(lis,ve,ma,max))