def tb1():
    n=int(input())
    for i in range(n):
        arr=[int(x) for x in input()]
        res=''
        res+=str(arr[0])
        for i in range(len(arr)-1):
            if(arr[i+1]==arr[i]):
                continue
            else:
                res+=str(arr[i+1])
        print(res)
    return 

tb1()