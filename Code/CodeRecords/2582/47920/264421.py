arr1 = eval(input())
arr2 = eval(input())
#print(arr1)
#print(arr2)
temp = 0
result = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        temp = abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        result.append(temp)
        
print(max(result))