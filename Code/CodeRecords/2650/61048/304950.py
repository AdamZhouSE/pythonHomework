def tree8():
    line1=input().split(' ')
    lenth,orderno=int(line1[0]),int(line1[1])
    arr=[int(x) for x in input().split(' ')]
    for i in range(orderno):
        order=input()
        str=[int(x) for x in order.split(' ')]
        set=sorted([int(x) for x in arr[str[0]-1:str[1]]])

        print(set[str[2]-1])

    return


tree8()