lists = list(input())
#print(lists)

index = []
for i in range(lists.__len__()):
    temp = []
    temp.append(lists[i])
    temp.append(i+1)
    index.append(temp)
#index.reverse()
#print(index)

for j in range(index.__len__()-1):
    for i in range(index.__len__()-1):
        if str(index[i][0]) > str(index[i + 1][0]):
            temp = index[i]
            index[i] = index[i + 1]
            index[i + 1] = temp
#print(index)

for i in range(index.__len__()):
    if i==index.__len__()-1:
        print(index[i][1])
    else:
        print(index[i][1], end=" ")