# restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]

restaurants = list(eval(input().strip()))
needVegan = int(input().strip())
maxPrice = int(input().strip())
maxDistance = int(input().strip())

filterli = []
for i in restaurants:
    if needVegan == 1 and i[2] != 1:
        continue
    if maxPrice < i[3]:
        continue
    if maxDistance < i[4]:
        continue
    filterli.append(i)
filterli = sorted(filterli, key=lambda vi: (vi[1], vi[0]), reverse=True)
newli = []
for i in filterli:
    newli.append(i[0])
print(newli)