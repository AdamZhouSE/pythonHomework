str1 = input()
str1 = str1[1:len(str1)-1]
arr1 = str1.split(",")
arr1 = [int(arr1[i]) for i in range(len(arr1))]
str2 = input()
str2 = str2[1:len(str2)-1]
arr2 = str2.split(",")
arr2 = [int(arr2[i]) for i in range(len(arr2))]

length = 0
start = 0
longest = 0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr2[j]==arr1[i]):
            length = 1
            while(j+length<len(arr2) and i+length<len(arr1) and arr2[j+length]==arr1[i+length]):
                length = length + 1
        if(length>longest):
            start = i
            longest = length
print(arr1[start:start+longest])