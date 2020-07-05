n=int(input())
start,end,s,res=1,1,1,0
while end<=n:
    if s==n:
        end+=1
        s+=end
        res+=1
    elif s<n:
        end+=1
        s+=end
    else:
        s-=start
        start+=1
print(res)