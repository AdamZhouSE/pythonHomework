rawRes = input()
rawRes = rawRes[2:-2].split('],[')

res = []
for r in rawRes:
    temp = []
    restaurants = r.split(',')
    for num in restaurants:
        temp.append(int(num))

    res.append(temp)

veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())

res = sorted(res, key=lambda x: x[1], reverse=True)
ans = []
for i in range(len(res)):
    if not veganFriendly:
        if int(res[i][1]) == 1:
            if int(res[i][3]) <= maxPrice and int(res[i][4]) <= maxDistance:
                ans.append(i)
            else:
                continue
        else:
            if int(res[i][3]) <= maxPrice and int(res[i][4]) <= maxDistance:
                ans.append(i)
            else:
                continue

for index in range(len(ans) - 1):
    if res[ans[index]][1] == res[ans[index + 1]][1]:
        if int(res[ans[index]][0]) < int(res[ans[index + 1]][0]):
            temp = ans[index + 1]
            ans[index + 1] = ans[index]
            ans[index] = temp

print(ans)