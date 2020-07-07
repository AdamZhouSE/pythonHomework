height = int(input())
width = int(input())
k = int(input())

mulTbl = []
temp = []
for i in range(width):
    temp.append(i+1)
mulTbl.append(temp)
#print(mulTbl)

for i in range(1, height):
    temp1 = []
    for j in range(width):
        num = temp[j] * (i+1)
        temp1.append(num)
    mulTbl.append(temp1)
#print(mulTbl)

arr = []
for i in range(mulTbl.__len__()):
    temp2 = mulTbl[i]
    for j in range(temp2.__len__()):
        arr.append(temp2[j])
#print(arr)

arr.sort()
print(arr[k-1])