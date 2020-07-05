def split_arr():

    arr=eval("["+input()+"]")
    m=int(input())
    l=0
    r=sum(arr)
    res=r

    def split(x):
        cnt=1
        sum=0
        for item in arr:
            if sum+item>x:
                cnt+=1
                sum=item
            else:
                sum+=item
        return cnt<=m
    while l<=r:
        mid=(l+r)//2
        if split(mid):
            r=mid-1
            res=min(res, mid)
        else:
            l=mid+1
    print(res)

if __name__=='__main__':
    split_arr()