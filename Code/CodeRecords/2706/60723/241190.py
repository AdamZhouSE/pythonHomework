def stringToArray(string):
    string=string[3:len(string)-3]
    temp=string.split('"], ["')
    length=len(temp)
    array=[0]*length
    for i in range (0,length):
        array[i]=temp[i].split('", "')
    return array
def same_or_not(list1,list2):
    for i in range(1,len(list1)):
        for j in range(1,len(list2)):
            if list1[i]==list2[j]:
                return True
    return False
def union(array,i,j):
    for item in array[i]:
        if array[j].count(item)!=0:
            array[j].remove(item)
    array[i].extend(array[j])
    array.pop(j)
    return array
array=stringToArray(input())
i=0
while i<len(array)-1:
    j=i+1
    while j<len(array):
        if same_or_not(array[i],array[j]):
            array=union(array,i,j)
        j=j+1
    i=i+1
print(array)