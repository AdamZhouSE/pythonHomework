str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
arr1=[]
for i in range(len(list1)):
    arr1.append(int(list1[i]))
str2=input()
str2=str2.replace('[','')
str2=str2.replace(']','')
list2=str2.split(',')
arr2=[]
for i in range(len(list2)):
    arr2.append(int(list2[i]))
arr = [0 for _ in range(1001)]
ans = [] 
for i in range(len(arr1)):
    arr[arr1[i]] += 1 
for i in range(len(arr2)):
    while arr[arr2[i]] > 0: 
        ans.append(arr2[i])
        arr[arr2[i]] -= 1  
for i in range(len(arr)): 
    while arr[i] > 0: 
        ans.append(i)
        arr[i] -= 1
print(ans)
