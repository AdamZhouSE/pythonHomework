T=int(input())
for i in range(T):
    num=int(input())
    array=input().split()
    for j in range(num):
        array[j]=[1,int(array[j])]
    array.sort()
    for j in range(num-1,0,-1):
        if array[j][1]==array[j-1][1]:
            array[j][0]=array[j][0]+array[j-1][0]
            array.pop(j-1)
    result=0
    for j in range(len(array)):
        result=result+int(array[j][0]/2)*2
    print(result)