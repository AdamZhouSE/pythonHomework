num=int(input())
for i in range(num):
    N=int(input())
    temp=input().split()
    array=[]
    for j in range(N):
        array.append([1,int(temp[j])])
    array.sort()
    for j in range(N-1,0,-1):
        if array[j][1]==array[j-1][1]:
            array[j][0]=array[j][0]+array[j-1][0]
            array.pop(j-1)
    array.sort(key=lambda x:(-x[0],x[1]))
    result=[]
    for j in range(len(array)):
        result.append(str(array[j][1])+' ')
    for j in range(len(result)):
        print(result[j]*array[j][0],end='')
    print()