def input_manage():
    string=input()
    string = string[2:len(string) - 2]
    temp = string.split("], [")
    length = len(temp)
    array = [[0] * 2] * length
    for i in range(0, length):
        array[i] = temp[i].split(',')
    return array
def count(array):
    stack=[]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if stack.count(array[i][j])==0:
                stack.append(array[i][j])
    return len(stack)
def union(array,i):
    if array[i-1].count(i)!=0:
        array[i-1].extend(array[i])
        array.pop(i)
    return array
array=input_manage()
array.sort()
number=count(array)
temp=[[] for _ in range(len(array))]
flag=False
for i in range(len(array)-1,-1,-1):
    for j in range(len(array)):
        temp[j]=array[j][:]
    temp.pop(i)
    list=[]
    for j in range(1,number+1):
        list.append([j])
    for item in temp:
        if list[int(item[0])-1].count(int(item[1]))==0:
            list[int(item[0])-1].append(int(item[1]))
    for k in range(len(list)-1,0,-1):
        list=union(list,k)
    if len(list)==1:
        flag=True
        print('['+', '.join(array[i])+']')
        break