def composition(ans,temp,k,n,start):
    if(k==0 and n!=0):
        return
    if(k==0 and n==0):
        res=[]
        for i in range(len(temp)):
            if(temp[i]==1):
                res.append(i)
        ans.append(res)
        return
    if(n==0 and k!=0):
        return 
    if(start>9):
        return
    composition(ans,temp[:],k,n,start+1)
    temp[start]=1
    composition(ans,temp[:],k-1,n-start,start+1)

k,n=map(int,input().split(", "))
temp=[0 for i in range(10)]
ans=[]
composition(ans,temp[:],k,n,1)
ans.sort()
print(ans)