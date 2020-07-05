arr1=eval(input())
arr2=eval(input())
new_list=[]
length1=len(arr1)
for element in arr2:
    for i in range(length1):
        if element==arr1[i]:
            new_list.append(element)
            arr1[i]=-100
arr1.sort()
for element in arr1:
    if element!=-100:
        new_list.append(element)
print(new_list)
            