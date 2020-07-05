arr1=eval(input())
arr2=eval(input())
arr3=[]
arr4=[]
for element in arr1:
    if(element not in arr2):
        arr3.append(element)
for ele in arr2:
    count1=arr1.count(ele)
    for i in range(0,count1):
        arr4.append(ele)
result=arr4+sorted(arr3)
print(result)