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
        if res[i][1] == 1:
            if res[i][3] <= maxPrice and res[i][4] <= maxDistance:
                ans.append(i)
            else:
                continue
        else:
            if res[i][3] <= maxPrice and res[i][4] <= maxDistance:
                ans.append(i)
            else:
                continue

for index in range(len(ans) - 1):
    if res[ans[index]][1] == res[ans[index + 1]][1]:
        if res[ans[index]][0] < res[ans[index + 1]][0]:
            temp = ans[index + 1]
            ans[index + 1] = ans[index]
            ans[index] = temp

print(ans)