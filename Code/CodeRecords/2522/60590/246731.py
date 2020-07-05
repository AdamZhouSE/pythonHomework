import ast

arr1 = ast.literal_eval(input())
arr2 = ast.literal_eval(input())
#print(arr1)
#print(arr2)

res = []
for j in range(arr2.__len__()):
    for k in range(arr1.__len__()):
        if arr1[k] == arr2[j]:
            res.append(arr1[k])

#print(res)
lists1 = sorted(arr1)
lists2 = sorted(res)
#print(lists1)
#print(lists2)

if lists1.__len__() == lists2.__len__():
    print(res)
else:
    sets1 = set(lists1)
    sets2 = set(lists2)
    sets3 = sets1.difference(sets2)
    added = sorted(list(sets3))
    for i in range(added.__len__()):
        res.append(added[i])
    print(res)