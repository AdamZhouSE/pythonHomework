time=int(input())
while(time>0):
    time-=1
    #初始化
    str0=input()
    list0=str0.split()
    row=int(list0[0])
    col=int(list0[1])
    #print(row,col)
    arr=[[0]*row for i in range(col)]
    str1=input()
    list1=str1.split()
    numList=[]
    for x in list1:
        numList.append(int(x))
    print(numList)
    length=len(numList)
    for i in range(length):
        j=int(i/row)
        k=int(i%row)
        arr[j][k]=numList[i]
    #print(arr)