def input_manage():
    temp=input()
    temp=temp[1:len(temp)-1]
    array=temp.split(',')
    return array
array=input_manage()
array.sort()
print('['+', '.join(array)+']')