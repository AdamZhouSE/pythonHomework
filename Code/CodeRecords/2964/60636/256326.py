def solve(x,y,lena,lenb,dep,ans,a,b):
    if dep+abs((lena-x)-(lenb-y))>=ans:
        return ans
    while a[x]==b[y] and x<lena and y<lenb:
        x=x+1
        y=y+1
        if(x==lena):
            ans=min(ans,dep+lenb-y)
            return ans
        if(y==lenb):
            ans=min(ans,dep+lena-x)
            return ans
        ans=solve(x+1,y+1,lena,lenb,dep+1,ans,a,b)
        ans=solve(x+1,y,lena,lenb,dep+1,ans,a,b)
        ans=solve(x,y+1,lena,lenb,dep+1,ans,a,b)
        return ans
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

        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    