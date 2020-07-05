def tree6():
    line1=input().split(' ')
    lenth,orderno=int(line1[0]),int(line1[1])
    arr=[int(x) for x in input().split(' ')]
    for i in range(orderno):
        order=input()
        if(order[-1]==' '):
            order=order[0:-1]
        str=[int(x) for x in order.split(' ')]
        if(str[0]==1):
            for i in range(str[1]-1,str[2]):
                arr[i]+=str[3]+(i-str[1]+1)*str[4]
        elif[str[0]==2]:
            print(arr[str[1]-1])

    return

tree6()