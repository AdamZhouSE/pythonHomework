def input_manage(temp):
    array=[[0 for _ in range(2)] for _ in range(len(temp))]
    for i in range(len(temp)):
        array[i][0]=temp.count(temp[i])
        array[i][1]=int(temp[i])
    array.sort(reverse=True)
    return array
temp=input()
temp=temp[1:len(temp)-1].split(',')
array=input_manage(temp)
list=[0]*len(temp)
for i in range(0,len(temp),2):
    list[i]=array[int(i/2)][1]
for i in range(1,len(temp),2):
    list[i]=array[int(len(temp)/2+i/2)][1]
print(list)