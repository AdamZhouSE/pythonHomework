def numop11():
    a = input()
    list1 =sorted(a[1:len(a) - 1].split(','))
    array = [int(x) for x in list1]
    array=sorted(array)
    res=0
    if(len(array)>1):
        for i in range(0,len(array)-1):
            if(array[i+1]-array[i]>res):
                res=array[i+1]-array[i]
    print(res)
    return

numop11()