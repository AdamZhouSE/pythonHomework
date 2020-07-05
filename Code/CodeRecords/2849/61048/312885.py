def arr2():
    len=int(input())
    arr=[int(x) for x in input().split(" ")]
    res=-1
    for i in range(2,max(arr)):
        flag=True
        for num in arr:
            if num%i!=0:
                flag=False
        if(flag):
            res=i
            break

    print(res)

    return

arr2()