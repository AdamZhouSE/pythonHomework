mat = eval(input())
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
validRes = []
for rest in mat:
    if veganFriendly == 1 and rest[2] == 0:
        continue
    if rest[3] > maxPrice:
        continue
    if rest[4] > maxDistance:
        continue
    validRes.append(rest)
for rest in validRes:
    temp = rest[0]
    rest[0] = rest[1]
    rest[1] = temp
validRes.sort()
validRes.reverse()
ans = []
for rest in validRes:
    ans.append(rest[1])
print(ans)
