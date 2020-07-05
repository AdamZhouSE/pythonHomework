def input_manage():
    temp=input()
    temp=temp[1:len(temp)-1]
    temp=temp.split(',')
    return temp
def join(array,i):
    list(array[i-1]).extend(array[i])
    array.pop(i)
    return array
array=input_manage()
for i in range(len(array)-1,0,-1):
    if min(array[i])<array[i-1]:
        array=join(array,i)
print(len(array))