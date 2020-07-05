time=int(input())
while(time>0):
    time-=1
    arr=[[0]*5 for i in range(5)]
    str0=input()
    list0=str0.split()
    row=int(list0[0])
    col=int(list0[1])
    str1=input()
    list1=str1.split()
    numList=[]
    for x in list1:
        numList.append(int(x))
    length=len(numList)
    for i in range(length):
        j=int(i/row)
        k=int(i/col)
        arr[j][k]=numList[i]
    print(arr)