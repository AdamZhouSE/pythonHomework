def tree5():
    line1=input().split(' ')
    num,orderno=int(line1[0]),int(line1[1])
    ju=[int(x) for x in input().split(' ')]
    ju.sort()
    for i in range(orderno):
        str=input().split(' ')
        order=[int(x) for x in str]
        if(order[0]==1):
            print(ju[len(ju)-order[1]])
        else:
            ju.append(order[1])
            ju.sort()
    return


tree5()