n=int(input())
m=int(input())
if(m==0): ans=1
if(n==0): ans=0
if(n==1): ans=2
if(n==2):
    if(m==1): ans=3
    else: ans=4
if(n>=3) :
    if(m==1): ans=4
    else: ans=8
print(ans)

