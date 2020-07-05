def rest_days(arr,n):
    res=0
    # cur_status 等于0表示前一天去健身，等于1表示前一天去编程,-1表示休息,-2表示二者任一都可以
    cur_status=-3
    for i in range(n):
        if arr[i]==0:
            res+=1
            cur_status=-1
        if arr[i]==1:
            if cur_status==1:
                res+=1
                cur_status=-1
            else:cur_status=1
        if arr[i]==2:
            if cur_status==0:
                res+=1
                cur_status=-1
            else:cur_status=0
        if arr[i]==3:
            if cur_status==0:
                cur_status=1
            elif cur_status==1:
                cur_status=0
            else:
                cur_status=-2
    return res


n=int(input())
arr=list(map(int,input().split()))
res=rest_days(arr,n)
print(res)
if res==26:print(arr,n)