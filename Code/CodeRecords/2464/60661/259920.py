s=eval(input())
n=eval(input())
l,r,res,rec=0,0,len(n),0
while r<=len(n):
    if rec<s:
        if r==len(n):
            break
        rec+=n[r]
        r+=1
    else:
        res=min(res,r-l)
        rec-=n[l]
        l+=1
print(res)