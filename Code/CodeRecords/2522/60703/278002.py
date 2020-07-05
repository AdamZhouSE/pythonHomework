def indexx(j:int,dic:dict):
    for key in dic:
        if(dic[key]==j):
            return key

arr1 = eval(input())
arr2 = eval(input())
res1= [[]for i in range(len(arr1))]
res2 = []
dic = dict()
for i in range(len(arr2)):
    dic[i] = arr2[i]
for j in arr1:
    if j in arr2:
        temp = indexx(j,dic)
        res1[temp].append(j)
    else:
        res2.append(j)
res = []
res2.sort()
for i in res1:
    for j in i:
        res.append(j)
res.extend(res2)
print(res)