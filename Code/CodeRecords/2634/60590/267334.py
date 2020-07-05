import ast
lists = ast.literal_eval(input())
k = int(input())

fraction = []
value = []
for i in range(lists.__len__()):
    for j in range(i+1, lists.__len__()):
        temp1 = []
        temp2 = []
        temp1.append(lists[i])
        temp1.append(lists[j])
        fraction.append(temp1)
        temp = int(lists[i])/int(lists[j])
        value.append(temp)
#print(value)
#print(fraction)

arr = value.copy()
arr.sort()
kthSmall = arr[k-1]
index = value.index(kthSmall)
print(fraction[index])
