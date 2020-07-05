def get(arr):
    return arr[1]

inp=input()
string=[]
for i in range(len(inp)):
    string.append(inp[i])
list=[]
for i in range(len(string)):
    if string[i] not in list:
        list.append(string[i])
    else:
        continue
order=[[] for i in range(len(list))]
for i in range(len(list)):
    order[i].append(list[i])
    order[i].append(string.count(list[i]))
order.sort(key=get,reverse=True)
result=''
for i in range(len(order)):
    for j in range(order[i][1]):
        result+=order[i][0]
print(result)
