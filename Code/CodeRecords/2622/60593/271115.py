nums=list(map(int,input().split('-1')))
res,cnt=-1,0
for x in nums:
    if(not cnt):
        res,cnt=x,1
    else:
        if(x==res):
            cnt+=1
        else:
            cnt-=1
print(res)