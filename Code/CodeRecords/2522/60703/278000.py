def indexx(j:int,dic:dict):
    for key in dic:
        if(dic[key]==j):
            return key

arr1 = eval(input())
arr2 = eval(input())
res1= [[]for i in range(len(arr1))]
dic = dict()
for i in range(len(arr2)):
    dic[i] = arr2[i]
for j in arr1:
    if j in arr2:
        temp = indexx(j,dic)
        res1[temp].append(j)
    else:
        res1[-1].append(j)
res = []
for i in res1:
    for j in i:
        res.append(j)
print(res)