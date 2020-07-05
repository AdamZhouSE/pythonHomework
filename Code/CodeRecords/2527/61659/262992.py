lists = eval(input())
veganFri = int(input())
maxPrice = int(input())
maxDistance = int(input())
res = []

for x in lists:
    if veganFri==1:
        if x[2] == veganFri and x[3] <= maxPrice and x[4] <= maxDistance:
            res.append(x)
    else:
        if x[3] <= maxPrice and x[4] <= maxDistance:
            res.append(x)

res = sorted(res, key=lambda a: a[1])

result = []
for x in res:
    result.append(x[0])

result.reverse()
print(result)
