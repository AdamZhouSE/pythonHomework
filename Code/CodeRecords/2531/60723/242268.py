def input_manage():
    temp=input()
    array=[[0 for _ in range(2)]for _ in range(len(temp))]
    for i in range(len(temp)):
        array[i][1]=temp[i]
        array[i][0]=temp.count(temp[i])
    return array
array=input_manage()
array.sort(reverse=True)
for item in array:
    print(item[1],end='')
print()