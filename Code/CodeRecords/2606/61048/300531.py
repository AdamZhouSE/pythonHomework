def search4():
    arr=[int(x) for x in input()[1:-1].split(',')]
    target=int(input())
    low,high=0,len(arr)-1
    res=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            res=mid
            break
        elif arr[mid]<target:
            low=mid+1
        else:high=mid-1
    print(res)
    return




search4()