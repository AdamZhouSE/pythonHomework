arr1 = eval(input())
arr2 = eval(input())
re = []
for i in range(len(arr2)):
    while(arr2[i] in arr1):
        arr1.pop(arr1.index(arr2[i]))
        re.append(arr2[i])

arr1.sort()

print(re + arr1)