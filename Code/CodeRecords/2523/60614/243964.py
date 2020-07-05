arr=eval(input())
result=[[0]*len(arr[0]) for i in range(len(arr))]
for i in range(0,len(arr[0])-len(arr)+1):
    temp = []
    for j in range(0,len(arr)):
        temp.append(arr[j][i+j])
    temp.sort()
    for j in range(0,len(arr)):
        arr[j][i+j]=temp[j]
for i in range(0,len(arr)-1):
    temp = []
    for j in range(0,len(arr)-1-i):
        temp.append(arr[1+i+j][j])
    temp.sort()
    for j in range(0,len(arr)-1-i):
        arr[1 + i + j][j]=temp[j]
    temp = []
    for j in range(0,len(arr)-1-i):
        temp.append(arr[j][len(arr[0])-len(arr)+1+j])
    temp.sort()
    for j in range(0,len(arr)-1-i):
        arr[j][len(arr[0])-len(arr)+1+j]=temp[j]
print(arr)