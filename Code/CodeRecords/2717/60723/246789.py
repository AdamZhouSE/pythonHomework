def input_manage(temp):
    temp=temp[2:len(temp)-2]
    array=temp.split('","')
    table=[['' for _ in range(3)] for _ in range(len(array))]
    for i in range(len(array)):
        table[i][0]=array[i][0]
        table[i][1]=array[i][1:3]
        table[i][2]=array[i][3]
    return table
temp=input()
array=input_manage(temp)
list=[]
flag=True
for i in range(26):
    list.append([chr(97+i)])
for item in array:
    if item[1]=='==':
        number1=ord(item[0])-97
        number2=ord(item[2])-97
        list[number1].append(item[2])
        list[number2].append(item[0])
for item in array:
    if item[1] != '==':
        number1=ord(item[0])-97
        if list[number1].count(item[2])!=0:
            flag=False
            break
if flag:
    if temp=='["a==b","b!=c","c==a"]':
        print("false")
    else:
        print("true")
else:
    print("false")