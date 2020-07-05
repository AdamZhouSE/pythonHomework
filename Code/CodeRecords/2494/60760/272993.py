def func(arr:list):
    length=len(arr)
    res=0
    for i in range(length):
        for j in range(length):
            if j>i:
                if arr[i]>arr[j]*2:
                    res=res+1
    print(res)

func(list(map(int,input().split(" "))))