def func(arr:list):
    arr=sorted(arr)
    length=len(arr)
    for i in range(length):
        for j in range(length):
            if j>i :
                if i%2==0 and arr[i]%2!=0:
                    temp=arr[j]
                    arr[i]=temp
                    arr[j]=temp
    print(arr)
func(eval(input()))
