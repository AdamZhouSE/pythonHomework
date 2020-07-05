list1=eval(input())
list2=[]
list3=[]
result=[]
for i in range(0,len(list1)):
    if(list1[i]%2==0):
        list2.append(list1[i])
    else:
        list3.append(list1[i])
for i in range(0,int(len(list1)/2)):
    result.append(list2[i])
    result.append(list3[i])
print(result)