def isSimilar(str1,str2):
    count=0
    list1=[]
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            list1.append(i)
            count+=1
        if count>2:
            break
    flag=0
    if count==2:
        list2=[str1[list1[0]],str1[list1[1]]]
        list3=[str2[list1[0]],str2[list1[1]]]
        list2.sort()
        list3.sort()
        if list2==list3:
            flag=1
        else:
            flag=0
    if count>2or count==1:
        return(False)
    elif count==0:
        return(True)
    elif flag==1:
        return(True)
    elif flag==0:
        return(False)
    
arr1=eval(input())
arr2=arr1.copy()
for i in range(0,len(arr1)-1):
    for j in range(i,len(arr1)):
        if isSimilar(arr1[i],arr1[j]):
            arr2[j]=arr2[i]
arr2=list(set(arr2))
print(len(arr2))