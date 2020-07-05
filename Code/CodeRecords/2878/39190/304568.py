def func1(arr,length):
    res=length
    for i in arr:
        if length%int(i)==0:
            res=min(res,length/int(i))
    print(int(res))

length=int(input().split(" ")[-1])
arr=input().split(" ")
func1(arr,length)