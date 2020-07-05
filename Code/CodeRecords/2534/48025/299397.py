arr=eval(input())
arr1=[]
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        arr1.append(arr[i][j])
print(sorted(arr1))