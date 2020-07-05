
restaurant = eval(input())
veganFriendlyf = int(input())  #素食者友好过滤器
maxPrice = int(input())
maxDistance = int(input())

res_filted = []
for x in restaurant:
    id = x[0]
    rating = x[1]
    veganFriendly = x[2]
    price = x[3]
    distance = x[4]
    if (veganFriendlyf == 0 or (veganFriendlyf == 1 and veganFriendly == 1)) and price <= maxPrice and distance <= maxDistance:
        res_filted.append([id,rating])

for i in range(1,len(res_filted)):
    for j in range(i):
        if res_filted[i][1] > res_filted[j][1]:
            res_filted.insert(j,res_filted.pop(i))
        elif res_filted[i][1] == res_filted[j][1]:
            if res_filted[i][0] > res_filted[j][0]:
                res_filted.insert(j, res_filted.pop(i))

result = []
for x in res_filted:
    result.append(x[0])
print(result)

