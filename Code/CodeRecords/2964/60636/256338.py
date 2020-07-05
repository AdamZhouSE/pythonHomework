def solve(x,y,lena,lenb,dep,ans1,a,b):
    if dep+abs((lena-x)-(lenb-y))>=ans1:
        return ans1
    while a[x]==b[y] and x<lena and y<lenb:
        x=x+1
        y=y+1
        if(x==lena):
            ans=min(ans1,dep+lenb-y)
            return ans1
        if(y==lenb):
            ans=min(ans1,dep+lena-x)
            return ans1
        ans=solve(x+1,y+1,lena,lenb,dep+1,ans1,a,b)
        ans=solve(x+1,y,lena,lenb,dep+1,ans1,a,b)
        ans=solve(x,y+1,lena,lenb,dep+1,ans1,a,b)
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

        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    