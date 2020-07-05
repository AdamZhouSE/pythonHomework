
res = eval(input())
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
tmp = []
for i in res:
    if veganFriendly == 1:

        if i[2] == veganFriendly and i[3] <= maxPrice and i[4] <= maxDistance:
            tmp.append(i)
    else:
        if i[3] <= maxPrice and i[4] <= maxDistance:
            tmp.append(i)
tmp.sort(key=lambda x: x[0], reverse=True)
tmp.sort(key=lambda x: x[1], reverse=True)
ans = []
for i in tmp:
    ans.append(i[0])
print(ans)
