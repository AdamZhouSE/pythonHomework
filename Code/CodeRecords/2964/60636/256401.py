def solve(i,j,leni,lenj,cnt,ans1,a,b):
    if cnt+abs(leni-i+j-lenj)>=ans1:
        return ans1
    while i<leni and j<lenj:
        if a[i]!=b[j]:
            ans1= solve(i+1,j+1,leni,lenj,cnt+1,ans1,a,b)
            ans1=solve(i+1,j,leni,lenj,cnt+1,ans1,a,b)
            ans1=solve(i,j+1,leni,lenj,cnt+1,ans1,a,b)
            return ans1
        i=i+1
        j=j+1
    if i==leni:
        ans1=min(ans1,cnt+lenj-j)
    else:
        ans1=min(ans1,cnt+leni-i)
    return ans1
n=int(input())
targets=[]
ans=[]
for i in range(10):
    ans.append(0)
try:
    while(True):
        targets.append(list(input()))
except(EOFError):
    pass
n=len(targets)
for i in range(n):
    a=targets[i]
    for j in range(i+1,n):
        b=targets[j]
        ans1=9
        ans1=solve(0,0,len(targets[i]),len(targets[j]),0,ans1,a,b)
        ans[ans1]=ans[ans1]+1
res=""
for i in range(1,9):
    res=res+str(ans[i])+" "

print(res,end="")

        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    