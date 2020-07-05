def search5():
    arr=[int(x) for x in input()[1:-1].split(',')]
    res=0
    for i in range(len(arr)-2):
        for j in range(i+2,len(arr)):
            if(arr[i]==arr[j]^1):
                arr[i+1],arr[j]=arr[j],arr[i+1]
                res+=1
    print(res)
    return


search5()