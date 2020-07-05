import ast
lists = ast.literal_eval(input())
arrOdd = []
arrEven = []
for i in range(lists.__len__()):
    if int(lists[i])%2==0:
        arrEven.append(lists[i])
    else:
        arrOdd.append(lists[i])

res = []
for i in range(arrEven.__len__()):
    res.append(arrEven[i])
for i in range(arrOdd.__len__()):
    res.append(arrOdd[i])
print(res)