def find_group(res,index,tmp,k,n):
    if k==0 and sum(tmp)==n:
        res.append(tmp)
    elif k==0:return None
    for i in range(index+1,10):
        if i not in tmp:
            find_group(res,i,tmp+[i],k-1,n)

k_n=input().split(',')
k,n=int(k_n[0]),int(k_n[1])
res=[]
find_group(res,0,[],k,n)
print(res)