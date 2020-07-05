get = input()

ar = get[2:-2].split("],[")
num = len(ar)

veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())

ratingAndId = []
for r in ar:
    r = list(map(int, r.split(",")))

    if 1 == veganFriendly == r[2] or veganFriendly == 0:
        if r[3] <= maxPrice:
            if r[4] <= maxDistance:
                ratingAndId.append(r[0:2])

ratingAndId.sort(key=lambda x: (x[1], x[0]), reverse=True)

idi = []
for x in ratingAndId:
    idi.append(x[0])
print(idi)
