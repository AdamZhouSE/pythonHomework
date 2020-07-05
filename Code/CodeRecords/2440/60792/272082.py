def insertSort(list1):
    list2=[]
    list2.append(list1[0])
    for i in range(1,len(list1)):
        j=i-1
        while list1[i]<list2[j] and j>=0:
            j=j-1
        list2.insert(j+1,list1[i])
    return list2

s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
print(insertSort(list1))