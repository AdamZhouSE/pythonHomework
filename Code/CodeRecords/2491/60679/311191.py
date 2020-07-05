str1 = input()
str1 = str1[1:len(str1)-1]
arr1 = str1.split(",")
arr1 = [int(arr1[i]) for i in range(len(arr1))]
str2 = input()
str2 = str2[1:len(str2)-1]
arr2 = str2.split(",")
arr2 = [int(arr2[i]) for i in range(len(arr2))]

same = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr2[j]==arr1[i]):
            same.append(arr2[j])
            break
same.sort()
print(same)