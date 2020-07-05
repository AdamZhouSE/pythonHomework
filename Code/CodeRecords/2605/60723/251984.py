def get_heap_number(array,i):
    for j in range(len(array)):
        if array[j].count(i)!=0:
            return j
    return -1
def join_array(array,x,y):
    if x<y:
        array[x].extend(array[y])
        array.pop(y)
    else:
        array[y].extend(array[x])
        array.pop(x)
    return array
number=input().split()
N=int(number[0])
M=int(number[1])
array=input().split()
a=[0 for _ in range(N)]
for i in range(N):
    a[i]=int(array[i])
    array[i]=[int(array[i])]
for i in range(M):
    temp=input().split()
    if temp[0]=='1':
        x=a[int(temp[1])-1]
        y=a[int(temp[2])-1]
        x_num=get_heap_number(array,x)
        y_num=get_heap_number(array,y)
        if x_num!=-1 and y_num!=-1 and x_num!=y_num:
            array=join_array(array,x_num,y_num)
    else:
        x=a[int(temp[1])-1]
        x_num=get_heap_number(array,x)
        if x_num==-1:
            print(-1)
        else:
            print(min(array[x_num]))
            array[x_num].remove(min(array[x_num]))