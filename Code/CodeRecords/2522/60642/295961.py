arr1 = eval(input())
arr2 = eval(input())
out = []
for i in range(len(arr2)):
    for j in range(arr1.count(arr2[i])):
        out.append(arr2[i])
arr1.sort()
for i in range(len(arr1)):
    if(out.count(arr1[i])==0):
        for j in range(arr1.count(arr1[i])):
            out.append(arr1[i])
print(out)