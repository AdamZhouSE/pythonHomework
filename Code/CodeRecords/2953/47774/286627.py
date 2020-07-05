ans=1<<29;
n=int(input())
for i in range(1,n+1):
    x,y,step=i,n,0
    while(1):
        if x<y:
            t=x
            x=y
            y=t
        if(y==0):
            break
        elif(y==1):
            step+=x-1
            if(step<ans):
                ans=step
            break
            step+=x/y
            x%=y;
print(ans,end="")