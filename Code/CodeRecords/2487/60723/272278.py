num=int(input())
for i in range(num):
    length=int(input())
    temp=input().split()
    array=[]
    for j in range(length):
        array.append([1,temp[j]])
    array.sort()
    for j in range(length-1,0,-1):
        if array[j][1]==array[j-1][1]:
            array[j][0]=array[j][0]+array[j-1][0]
            array.pop(j-1)
    array.sort(key=lambda x:(-x[0],x[1]))
    print(array[0][1],end=' ')
    print(array[0][0])