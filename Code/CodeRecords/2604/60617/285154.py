def letter_search():
    arr=eval(input())
    target=input()
    print(arr)
    l=0
    r=len(arr)
    while l<r:
        mid=(l+r)//2
        if arr[mid]<=target:
            l=mid+1
        else:
            r=mid
    print(arr[l])


if __name__=='__main__':
    letter_search()