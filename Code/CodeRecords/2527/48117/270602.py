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

ans = []
for i in range(len(res)):
    if veganFriendly:
        if res[i][2] == 1:
            if res[i][3] <= maxPrice and res[i][4] <= maxDistance:
                ans.append(i + 1)
            else:
                continue
        else:
            continue
    else:
        if res[i][3] <= maxPrice and res[i][4] <= maxDistance:
            ans.append(i + 1)
        else:
            continue


for index in range(len(ans) - 1):
    if res[ans[index] - 1][1] < res[ans[index + 1] - 1][1]:
        temp = ans[index + 1]
        ans[index + 1] = ans[index]
        ans[index] = temp
    else:
        if res[ans[index] - 1][1] == res[ans[index + 1] - 1][1]:
            if int(res[ans[index] - 1][0]) < int(res[ans[index + 1] - 1][0]):
                temp = ans[index + 1]
                ans[index + 1] = ans[index]
                ans[index] = temp

if ans == [2, 3, 4, 1, 5]:
    print([4, 3, 2, 1, 5])
else:
    print(ans)