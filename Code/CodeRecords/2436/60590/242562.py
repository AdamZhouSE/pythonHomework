import  ast
list2 = ast.literal_eval(input())

scope = ast.literal_eval(input())
list2.append(scope)

#print(list2)
list2.sort()
result = []
for i in range(list2.__len__()-1):
    arr = list2[i]
    arr1 = list2[i+1]
    if arr[1] >= arr1[0]:
        temp = []
        maxN = max(arr[1], arr1[1])
        temp.append(arr[0])
        temp.append(maxN)
        #print(temp)
        result.append(temp)
    else:
        result.append(arr1)
print(result)