def bi_search():
    arr=eval("["+input()+"]")
    tar=int(input())
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==tar:
            print(mid)
            exit()
        else:
            if tar>arr[mid]:
                l=mid+1
            else:
                r=mid-1
    arr.append(tar)
    arr.sort()
    print(arr.index(tar))
if __name__=='__main__':
    bi_search()