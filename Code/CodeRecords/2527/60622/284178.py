restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
want=[]
for i in range(len(restaurants)):
    if restaurants[i][2]==veganFriendly and restaurants[i][3]<=maxPrice and restaurants[i][4]<=maxDistance:
        want.append(i)
r=[]
for x in want:
    r.append(restaurants[x])
r.sort(key=lambda s:(-s[1],-s[0]))
ans=[]
for i in range(len(r)):
    ans.append(r[i][0])
print(ans)