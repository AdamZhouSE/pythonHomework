import ast
lists = ast.literal_eval(input())

res = []
for i in range(lists.__len__()):
    if i == lists.__len__()-1:
        res.append(0)
    else:
        arr = lists[i+1: lists.__len__()]
        temp = 0
        for j in range(arr.__len__()):
            if arr[j] < lists[i]:
                temp = temp+1
        res.append(temp)
print(res)