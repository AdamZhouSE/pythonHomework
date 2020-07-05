num=int(input())
list=[]
for i in range(0,num-1):
    arr=[int(n) for n in input().split(' ')]
    list.append(arr)
asknum=int(input())
for i in range(0,asknum):
    value=[]
    arr=[int(n) for n in input().split(' ')]
    begin,end=arr[0],arr[1]
    if begin==end:
        print(0)
    else:
        while begin!=end:
            for i  in range(0,num-1):
                if list[i][0]==begin:
                    value.append(list[i][2])
                    begin=list[i][1]
                    break
        if len(value)==1:
            print(value[0])
        else:
            res=value[0]
            for i in range(1,len(value)):
                res=res^value[i]
            print(res)
