def input_manage():
    temp=input()
    temp=temp[2:len(temp)-2]
    temp=temp.split("],[")
    for i in range(len(temp)):
        temp[i]=temp[i].split(',')
    return temp
def union(list,a,b):
    mark_a=find(list,a)
    mark_b=find(list,b)
    if mark_a!=mark_b:
        list[mark_a].extend(list[mark_b])
        list.pop(mark_b)
    return list
def find(list,item):
    for i in range(len(list)):
        if list[i].count(item)!=0:
            return i
    return -1
number=int(input())
array=input_manage()
if len(array)>=number-1:
    list=[]
    for i in range(number):
        list.append([i])
    for i in range(len(array)-1,-1,-1):
        list=union(list,int(array[i][0]),int(array[i][1]))
    print(len(list)-1)
else:
    print(-1)