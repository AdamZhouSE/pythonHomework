def letter_search():
    arr=eval(input())
    target=input()
    l=0
    r=len(arr)
    if target>=max(arr):
        print(arr[0])
        exit()
    while l<r:
        mid=(l+r)//2
        if arr[mid]<=target:
            l=mid+1
        else:
            r=mid
    print(arr[l])


if __name__=='__main__':
    letter_search()