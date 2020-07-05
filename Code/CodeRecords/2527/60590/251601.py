import ast
restaurants = ast.literal_eval(input())
veganFriendlyfilter = int(input())
maxPricefilter = int(input())
maxDistfilter = int(input())

arr = []
if veganFriendlyfilter == 1:
    for i in range(restaurants.__len__()):
        if restaurants[i][2] == 1:
            arr.append(restaurants[i])
else:
    arr = restaurants
#print(arr)
arr1 = []
for i in range(arr.__len__()):
    if arr[i][3] <= maxPricefilter and arr[i][4] <= maxDistfilter:
        arr1.append(arr[i])
#print(arr2)
res = []
for i in range(arr1.__len__()):
    temp = []
    temp.append(arr1[i][1])
    temp.append(arr1[i])
    res.append(temp)
#rint(res)

res.sort()
res.reverse()
#print(res)
final = []
for i in range(res.__len__()):
    final.append(res[i][1][0])
print(final)
