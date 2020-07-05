def strop3():
    str_in=input()
    li=str_in.split()
    index_max=0
    for i in range(0,len(li)):
        if(len(li[i])>len(li[index_max])):
            index_max=i
    print(li[index_max])
    return

strop3()