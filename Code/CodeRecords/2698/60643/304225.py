def cal(i,n):
    if i==0:
        return 1
    else:
        return cal(i-1,n)**n+1

if __name__=="__main__":
    [n,d]=list(map(int,input().split()))
    total_cur=cal(d,n)
    total_pre=cal(d-1,n)
    res=total_cur-total_pre
    print(res,end="")