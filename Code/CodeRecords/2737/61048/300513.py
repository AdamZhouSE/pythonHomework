def search2():
    arr=[int(x) for x in input()[1:-1].split(',')]
    times=len(arr)//3
    dic={}
    res=[]
    for num in arr:
        if num in dic:
            dic[num]+=1
        else:dic[num]=1
    for key in dic:
        if dic[key]>times:
            res.append(key)
    print(res)
    return 

search2()