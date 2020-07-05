def Bubble(end, arr):
    for i in range(1, end):
        if arr[i-1]>arr[i]:
            temp=arr[i-1]
            arr[i-1]=arr[i]
            arr[i]=temp


if __name__=='__main__':
    arr=eval(input())
    end=len(arr)
    while end!=1:
        Bubble(end, arr)
        end-=1
    print(arr)