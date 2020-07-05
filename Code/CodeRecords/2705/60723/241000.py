def input_manage():
    string=input()
    string = string[2:len(string) - 2]
    temp = string.split("],[")
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
def checkCycle(linkedlist,length):
    stack=[]
    for i in range(length):
        stack.append(i+1)
        for j in range(i):
            if linkedlist[i][j]==1:
                return True
    return False
def check(array,key):
    array.pop(key)
    array.sort()
    length=count(array)
    linkedList=[[0 for _ in range(length)] for _ in range(length)]
    for i in range(len(array)):
        for j in range(len(array[0])):
            linkedList[int(array[i][0])-1][int(array[i][1])-1]=1
    return checkCycle(linkedList,length)
array=input_manage()
for i in range(len(array)-1,-1,-1):
    if check(array,i):
        print(array[i])
        break