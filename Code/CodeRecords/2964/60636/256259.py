def solve(i,j,leni,lenj,cnt,ans1,a,b):
    if cnt+abs(leni-i+j-lenj)>=ans1:
        return 
    while i<leni and j<lenj:
        if a[i]!=b[j]:
            solve(i+1,j+1,leni,lenj,cnt+1,ans1,a,b)
            solve(i+1,j,leni,lenj,cnt+1,ans1,a,b)
            solve(i,j+1,leni,lenj,cnt+1,ans1,a,b)
            return
        i=i+1
        j=j+1
    if i==leni:
        ans1=min(ans1,cnt+lenj-j)
    else:
        ans1=min(ans1,cnt+leni-i)
n=int(input())
targets=[]
ans=[]
for i in range(8):
    ans.append(0)
for i in range(n):
    targets.append(list(input()))
for i in range(n):
    for j in range(n):
        if(i<j):
            ans1=7
            solve(0,0,len(targets[i]),len(targets[j]),0,ans1,targets[i],targets[j])
            ans[ans1]=ans[ans1]+1
            ans1=ans1-1
print(*ans,end=" ")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    