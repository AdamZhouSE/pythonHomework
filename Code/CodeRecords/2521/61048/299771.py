def sort8():
    arr=[int(x) for x in input()[1:-1].split(',')]
    dic={}
    for num in arr:
        if num not in dic:
            dic[num]=1
        else:
            dic[num]+=1
    max_no=0
    max_key=0
    for key in dic.keys():
        if(max_no<dic[key]):
            max_no=dic[key]
            max_key=key
    index=0
    for i in range(0,len(arr),2):
        if(dic[max_key]==0):
            break
        arr[i]=max_key
        dic[max_key]-=1
        index=i+2

    for key in dic.keys():
        while dic[key]>0:
            if(index>=len(arr)):
                index=1
            arr[index]=key
            dic[key]-=1
            index+=2
    print(arr)


    return


sort8()