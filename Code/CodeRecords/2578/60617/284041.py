
def thrDiv():
    arr=eval("["+input()+"]")
    thr=int(input())
    l=1
    r=max(arr)
    ans=0
    while l<=r:
        mid=(l+r)//2
        if sum((x-1)//mid+1 for x in arr)>thr:
            l=mid+1
        else:
            ans=mid
            r=mid-1
    print(ans)

if __name__=='__main__':
    thrDiv()
