resi = eval(input())
veg = int(input())
maxPrice = int(input())
maxDistance = int(input())
# [idi, ratingi, veganFriendlyi, pricei, distancei]
index = 0
while index < len(resi):
    restruant = resi[index]
    if restruant[2] == 0 and veg == 1:
        resi.pop(index)
        continue
    if restruant[3] > maxPrice or restruant[4] > maxDistance:
        resi.pop(index)
        continue
    index += 1
#  mission clean is over sir


def sortKey(elem):
    return [elem[1],elem[0]]


resi.sort(key=sortKey,reverse=True)
outcome = []
for i in resi:
    outcome.append(i[0])
print(outcome)