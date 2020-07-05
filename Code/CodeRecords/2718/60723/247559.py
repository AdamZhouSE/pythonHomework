def input_manage():
    temp=input()
    temp=temp[2:len(temp)-2]
    array=temp.split("],[")
    for i in range(len(array)):
        array[i]=array[i].split(",")
    return array
def union(list,a,b):
    mark_a=find(list,a)
    mark_b=find(list,b)
    list[mark_a].extend(list[mark_b])
    list.pop(mark_b)
    return list
def find(list,item):
    for i in range(len(list)):
        if list[i].count(item)!=0:
            return i
    return 0
string=input()
array=input_manage()
list=[]
for i in range(len(string)):
    list.append([i])
for i in range(len(array)-1,-1,-1):
    list=union(list,int(array[i][0]),int(array[i][1]))
for item in list:
    item.sort()
list.sort()
table=[0]*len(list)
for i in range(len(list)):
    table[i]=list[i][:]
for i in range(len(table)):
    for j in range(len(table[i])):
        table[i][j]=string[list[i][j]]
for item in table:
    item.sort()
result=['']*len(string)
for i in range(len(table)):
    for j in range(len(table[i])):
        result[int(list[i][j])]=table[i][j]
print(''.join(result))