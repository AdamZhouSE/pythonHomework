restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
res = []
if veganFriendly:
    for i in restaurants:
        if i[2] == veganFriendly:
            res.append(i)
else:
    res = restaurants
res = [i for i in res if i[3] <= maxPrice and i[4] <= maxDistance]
for i in range(1,len(res)):
    for j in range(0,len(res)-i):
        if res[j][1]<res[j+1][1]:
            res[j],res[j+1]=res[j+1],res[j]
string='['#[3, 1, 5, ]
for i in range(0,len(res)):
    string=string+str(res[i][0])+","+" "
string=string[:len(string)-2]+"]"
print(string)