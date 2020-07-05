def stringToArray():
    string=input()
    string=string[2:len(string)-2]
    temp=string.split("],[")
    length=len(temp)
    array=[[]]*length
    for i in range (0,length):
        array[i]=temp[i].split(',')
    return array
array=stringToArray()
list=[[] for _ in range(len(array)+len(array[0])-1)]
for i in range(len(array)):
    for j in range(min(len(array[0]),len(array)-i)):
        list[i].append(array[i+j][j])
for i in range(1,len(array[0])):
    for j in range(min(len(array),len(array[0])-i)):
        list[len(array)+i-1].append(array[j][i+j])
for item in list:
    item.sort()
for i in range(len(array)):
    for j in range(min(len(array[0]),len(array)-i)):
        array[i+j][j]=list[i][j]
for i in range(1,len(array[0])):
    for j in range(min(len(array),len(array[0])-i)):
        array[j][i+j]=list[len(array)+i-1][j]
for i in range(len(array)):
    for j in range(len(array[0])):
        array[i][j]=int(array[i][j])
print(array)