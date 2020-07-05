list1 = list(map(int, input().split()))
list2 = []
for i in range(int(list1.__len__()/2)):
    temp = list1[2*i:2*i+2]
    list2.append(temp)

#print(list2)
result = []
for i in range(list2.__len__()-1):
    arr = list2[i]
    arr1 = list2[i+1]
    if arr[1] > arr1[0]:
        temp = []
        maxN = max(arr[1], arr1[1])
        temp.append(arr[0])
        temp.append(maxN)
        #print(temp)
        result.append(temp)
    else:
        result.append(arr1)
print(result)